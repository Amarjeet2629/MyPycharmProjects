from django import views
from django.shortcuts import render
from django.views.generic import TemplateView


def Homepage(request):
    return render(request, 'homepage.html', {})
