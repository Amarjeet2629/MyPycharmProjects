from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from . import views

app_name = 'Entry'

urlpatterns = [
    url(r'^host_register/$', views.HostRegister, name='host_register'),
    url(r'^visitor_register/$', views.VisitorRegister, name='visitor_register'),
]