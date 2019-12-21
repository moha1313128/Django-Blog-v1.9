from django.http import HttpResponse
from django.shortcuts import render

def post_create(request):
	return HttpResponse("<h1>create</h1>")

def post_detail(request):
	return HttpResponse("<h1>detail</h1>")

def post_list(request):
	return HttpResponse("<h1>list</h1>")

def post_update(request):
	return HttpResponse("<h1>update</h1>")

def post_delete(request):
	return HttpResponse("<h1>delete</h1>")			
