from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf.urls import url
from django.contrib.auth import views as auth_views


app_name = 'groups'

urlpatterns = [
    url(r'^create/$', views.CreateGroup, name='create_group'),
    url(r'^group_list/$', views.GroupList, name='group_list'),
    url(r'^(?P<slug>.*)/$', views.GroupSingle, name='group_single'),
    url(r'^join/(?P<slug>.*)/$', views.GroupJoin, name='group_join')
]
