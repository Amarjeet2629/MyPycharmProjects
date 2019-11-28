from django.shortcuts import render
from django.http import HttpResponse
from .forms import NewUser
# Create your views here.


def start(request):
    my_dict = {'text':'hello world','number':100}
    return render(request, 'Login/start.html', my_dict)

def other(request):
    return render(request,'Login/other.html',{})

def relative(request):
    return render(request,'Login/relative_url_template.html',{})