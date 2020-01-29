from django.conf.urls import url
from django.contrib import admin

from .views import (
	post_list,
	post_create,
	post_detail,
	post_update,
	post_delete,
	)

urlpatterns = [
    #url(r'^posts/$', "posts.views.post_home"),		#url(r'^posts/$', <app_name>.views.<function_name>)
    url(r'^$', post_list, name="list"),
    url(r'^create/$', post_create),
    # url(r'^(?P<id>\d+)/$', post_detail, name='detail'), 
    url(r'^(?P<slug>[\w-]+)/$', post_detail, name='detail'),
    url(r'^(?P<slug>[\w-]+)/edit/$', post_update, name='update'),
    url(r'^(?P<slug>[\w-]+)/delete/$', post_delete),
]
