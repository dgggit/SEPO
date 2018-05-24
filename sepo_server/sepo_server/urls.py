"""sepo_server URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""


from django.conf.urls import include, url
from django.conf import settings
from django.contrib import admin
from django_markdown import flatpages
from django.conf.urls.static import static

admin.autodiscover()
flatpages.register()
urlpatterns = [
	url(r'^', include('mainpage.urls')),
    url(r'^admin/', include(admin.site.urls)),
	url(r'^community/', include('community.urls')),
	url(r'^user/', include('user_manager.urls')),
	url(r'^post/',include('writer.urls')),
	url(r'^ckeditor/', include('ckeditor_uploader.urls')),
] + static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
