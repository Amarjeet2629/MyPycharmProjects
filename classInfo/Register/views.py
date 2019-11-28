from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView, ListView, CreateView, DetailView
from . import models
# Create your views here.





class HomepageView(TemplateView):
    template_name = 'Register/index.html'


class DepartmentListView(ListView):
    model = models.Department


class StudentCreateView(CreateView):
    context_object_name = 'form'
    model = models.Student
    fields = ('name', 'roll', 'dept')


class DepartmentDetailView(DetailView):
    model = models.Department
    context_object_name = 'department_detail'


class StudentDetailView(DetailView):
    model = models.Student

