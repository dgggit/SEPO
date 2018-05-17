#from django.urls import path
from django.conf.urls import include,url
from user_manager.views import login#,login_validate
from . import views


urlpatterns = [
	url(r'^login/$',login),
	#url(r'^login/validate/$',login_validate),
]

