#from django.urls import path
from django.conf.urls import include,url
from community.views import post_community
from . import views


urlpatterns = [
#	path('', views.index, name = 'index'),
	url(r'^$',post_community),
]

