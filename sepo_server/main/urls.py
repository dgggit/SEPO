#from django.urls import path
from django.conf.urls import include,url
from main.views import mainpage

urlpatterns = [
	url('',mainpage),
]

