from django.shortcuts import render
from .forms import UserInfoForm, UserProfileInfoForm
# Create your views here.
from django.http import HttpResponseRedirect, HttpResponse
#from .forms import UserForm, UserProfileInfoForm
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

def index(request):
    return render(request, 'index.html', {})



def register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserInfoForm(data=request.POST)
        profile_form = UserProfileInfoForm(request.POST, request.FILES)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            registered = True
        else :
            print(profile_form.errors, user_form.errors)
    else:
        user_form = UserInfoForm()
        profile_form = UserProfileInfoForm()

    return render(request, 'register.html', {'user_form':user_form, 'profile_form':profile_form, 'registered':registered})


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))
            else:
                print('user not active')
        else:
            print("Pisssed offf")
    return render(request, 'login.html', {})