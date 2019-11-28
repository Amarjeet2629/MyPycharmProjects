from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from . import views

app_name = 'Login'

urlpatterns = [
    url(r'^$', views.index.as_view(), name='index'),
    url(r'^sign_up/$', views.register, name='register'),
    url(r'^login/', views.user_login, name='user_login')

]
