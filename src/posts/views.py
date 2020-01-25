from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .forms import PostForm
from .models import Post

def post_create(request):
	form = PostForm(request.POST or None)
	if form.is_valid():
		instance = form.save(commit=False)
		print (form.cleaned_data.get("title"))
		instance.save()
	# if request.method == "POST":
		# print ("Title" + request.POST.get("title"))
		# print ("Content" + request.POST.get("content"))
		# title = request.POST.get("title")
		# Post.objects.create(title=title)
	context = {
		"form": form,
	}
	return render(request, "post_form.html", context)
	# return HttpResponse("<h1>create</h1>")

def post_detail(request, id=None):
	# instance = Post.objects.get(id=90)
	instance = get_object_or_404(Post, id=id)
	context = {
		"title": instance.title,
		"instance": instance,
	}
	return render(request, "post_detail.html", context)
	# return HttpResponse("<h1>detail</h1>")

def post_list(request):
	queryset = Post.objects.all()
	context = {
		"object_list": queryset,
		"title": "list"
	}


	# if request.user.is_authenticated():
	# 	context = {
	# 		"title": "user list"
	# 	}
	# # changing the template also	
	# # return render(request, "index.html", context)	
	# else:
	# 	context = {
	# 		"title": "public list"
	# 	}	
	return render(request, "index.html", context)
	# return HttpResponse("<h1>list</h1>")

def post_update(request):
	return HttpResponse("<h1>update</h1>")

def post_delete(request):
	return HttpResponse("<h1>delete</h1>")			
