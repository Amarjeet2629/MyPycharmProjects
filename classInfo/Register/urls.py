from django.contrib import admin
from django.urls import path
from django.conf.urls import url,include
from Register import views

app_name = "Register"

urlpatterns=[
    url(r'^$', views.HomepageView.as_view(), name='HomepageView'),
    url(r'^lists/$', views.DepartmentListView.as_view(), name='deptlist'),
    url(r'^create/$', views.StudentCreateView.as_view(), name='student_create_view'),
    url(r'^lists/(?P<pk>\d+)/$', views.DepartmentDetailView.as_view(), name='detail'),
    url(r'^students/(?P<pk>\d+)/$', views.StudentDetailView.as_view(), name='stud_detail'),
]