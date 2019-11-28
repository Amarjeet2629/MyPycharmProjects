from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf.urls import url
from django.contrib.auth import views as auth_views

app_name = 'accounts'

urlpatterns = [

    url(r'^sign_up/$', views.sign_up, name='sign_up'),
    url(r'^login/$', auth_views.LoginView.as_view(template_name='../../social_copy1/templates/Login.html'), name='login'),
    url(r'^logout/$', auth_views.LogoutView.as_view(), name='logout'),

]
