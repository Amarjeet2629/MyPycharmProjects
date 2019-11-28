from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views

app_name = 'accounts'

urlpatterns = [
    url(r'^student_sign_up/$', views.StudentSignUp, name='student_sign_up'),
    url(r'^teacher_sign_up/$', views.TeacherSignUp, name='teacher_sign_up'),
    url(r'^logout/$', auth_views.LogoutView.as_view(), name='logout'),
    url(r'^login/$', views.UserLogin, name='login'),
    url(r'^(?P<username>[-\w]+)/$', views.ProfileSingle, name='profile_single'),
]
