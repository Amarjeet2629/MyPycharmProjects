from django.shortcuts import render
from django.http import HttpResponse
from . import forms
# Create your views here.


def index(request):
    my_dict = {}
    return render(request, 'form_app/index.html', my_dict)


def form_view(request):
    form = forms.UserInfo()
    if request.method == "POST":
        form = forms.UserInfo(request.POST)

        if form.is_valid():
            print("Form Validation is SUCCESS!!")
            print('Name: ' + form.cleaned_data['name'])
            print('Email: ' + form.cleaned_data['email'])
            print('Text: ' + form.cleaned_data['text'])
    return render(request, 'form_app/form.html', {'form': form})
