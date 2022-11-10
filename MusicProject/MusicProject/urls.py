"""MusicProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django import views
from django.contrib import admin
from django.urls import path , re_path
from django.urls.conf import include
from MusicApp.views import model_form_upload
from django.conf import settings
from django.conf.urls.static import static

from django.views.static import serve




urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('MusicApp.urls')),
    path('result/', model_form_upload, name='result'),

    re_path(r'^media/(?P<path>.*)$', serve,{'document_root':       settings.MEDIA_ROOT}), 
    re_path(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),
]   

#Handeling 404 error
#handler404 = 'MusicApp.views.handle_not_found'

#Handeling 500 error
#handler500 = 'MusicApp.views.handle_server_error'