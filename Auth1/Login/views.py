from django.shortcuts import render
from django.shortcuts import redirect, reverse
from django.views.generic import TemplateView, CreateView, ListView
from django.contrib.auth.views import LoginView
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from . import forms
# Create your views here.


class index(TemplateView):
    template_name = 'index.html'


def register(request):
    registered = False
    first_name = ''
    if request.method == "POST":
        user_form = forms.UserSignUpForm(data=request.POST)
        if user_form.is_valid() :
            user = user_form.save(commit=False)
            user.set_password(user.password)
            user.save()
            first_name = user.first_name
            registered = True
        else:
           raise ValueError(user_form.errors)
        
    else:
        user_form = forms.UserSignUpForm()
    
    return render(request, 'registration/register.html', {'user_form': user_form, 'registered': registered, 'first_name': first_name})


def user_login(request):

    user_name = request.POST.get('username')
    password = request.POST.get('password')

    user = authenticate(username=user_name, password=password)
    #print(user_name)
    if user is not None:
        if user.is_active:
           # print('Hi')
            login(request, user)
            return HttpResponseRedirect(reverse('Login:index'))
        else:
            print('Errors')
    else:
        return render(request, 'registration/login.html', {})