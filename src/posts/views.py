from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from .models import Post

def post_create(request):
	return HttpResponse("<h1>create</h1>")

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
		"title": "public list"
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
