from urllib.parse import urlencode, quote_plus
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib import messages
from .forms import PostForm
from .models import Post

def post_create(request):
	# if not request.user.is_staff or not request.user.is_superuser:
	# 	raise Http404

	# if not request.user.is_auhenticated:
	# 	raise Http404

	form = PostForm(request.POST or None, request.FILES or None)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.user = request.user 
		instance.save()
		messages.success(request, "Successfully Created", extra_tags='html_safe')
		return HttpResponseRedirect(instance.get_absolute_url())
			
	context = {
		"form": form,
	}
	return render(request, "post_form.html", context)

def post_update(request, slug=None):
	# if not request.user.is_staff or not request.user.is_superuser:
	# 	raise Http404
	instance = get_object_or_404(Post, slug=slug)
	form = PostForm(request.POST or None, request.FILES or None, instance=instance)
	if form.is_valid():
		instance = form.save(commit=False)
		print (form.cleaned_data.get("title"))
		instance.save()
		messages.success(request, "Successfully Edited", extra_tags='html_safe')
		return HttpResponseRedirect(instance.get_absolute_url())
	
	context = {
		"title": instance.title,
		"instance": instance,
		"form":  form,
	}
	return render(request, "post_form.html", context)

def post_detail(request, slug):
	instance = get_object_or_404(Post, slug=slug)
	share_string = quote_plus(instance.content)
	context = {
		"title": instance.title,
		"instance": instance,
		"share_string": share_string,
	}
	return render(request, "post_detail.html", context)

def post_list(request):
	queryset_list = Post.objects.all() #.order_by("-timestamp")
	paginator = Paginator(queryset_list, 3)
	page_request_var = "page"
	page = request.GET.get(page_request_var)
	try:
		queryset = paginator.page(page)
	except PageNotAnInteger:
		queryset = paginator.page(1)
	except EmptyPage:
		queryset = paginator.page(paginator.num_pages)

	context = {
		"object_list": queryset,
		"title": "List",
		"page_request_var": page_request_var
	}
	return render(request, "post_list.html", context)

def post_delete(request, slug=None):
	# if not request.user.is_staff or not request.user.is_superuser:
	# 	raise Http404
	instance = get_object_or_404(Post, slug=slug)
	instance.delete()
	messages.success(request, "Successfully Deleted")
	return redirect("posts:list")
