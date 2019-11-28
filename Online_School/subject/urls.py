from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from django.conf import settings
from . import views
from django.conf.urls.static import static

app_name = 'subject'
urlpatterns = [
    url(r'^course_list/$', views.CourseList, name='course_list'),
    url(r'^create/$', views.CourseCreate, name='course_create'),
    url(r'^(?P<slug>[-\w]+)/$', views.CourseDetail, name='course_detail'),
    url(r'^(?P<slug>[-\w]+)/join/$', views.CourseJoin, name='course_join'),
    url(r'^(?P<slug>[-\w]+)/leave/$', views.CourseLeave, name='course_leave'),
]
