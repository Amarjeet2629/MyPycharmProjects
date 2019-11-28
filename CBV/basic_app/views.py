from django.shortcuts import render
from django.views.generic import (View,ListView,DetailView,TemplateView,
                                  CreateView,UpdateView,DeleteView)
from django.http import HttpResponse
from . import models
from django.urls import reverse_lazy

class CBView(TemplateView):
    template_name = 'index.html'


class SchoolListView(ListView):
    context_object_name = 'schools'
    template_name = 'basic_app/schoollist.html'
    model = models.School


class SchoolDetailView(DetailView):
    context_object_name = 'school_detail'
    template_name = 'basic_app/schooldetail.html'
    model = models.School


class SchoolCreateView(CreateView):
    fields = ('name', 'principal', 'location')
    model = models.School


class SchoolUpdateView(UpdateView):
    fields = ('name', 'principal')
    model = models.School

class SchoolDeleteView(DeleteView):
    model = models.School
    success_url = reverse_lazy('basic_app:list')