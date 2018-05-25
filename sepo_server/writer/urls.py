
from django.conf.urls import include,url
from community.views import post_community
from . import views
from writer.views import test_writer, edit, delete, view


urlpatterns = [
	url(r'^upload/',test_writer),
#url(r'^(?P<pk>\d+)/',viewer, name = 'post_view'),
	url(r'^edit/(?P<pk>\d+)/',edit, name = 'post_edit'),
	url(r'^delete/(?P<pk>\d+)/',delete, name = 'post_delete'),
	url(r'^view/(?P<pk>\d+)/',view, name = 'post_view'),
]

