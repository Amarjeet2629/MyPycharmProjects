from django.shortcuts import render
from .forms import UserForm, UserProfileInfoForm
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import login, logout, authenticate
from django.urls import reverse
from django.contrib.auth.decorators import login_required
# Create your views here.


def index(request):
    return render(request, 'basic_app/index.html', {})


@login_required
def special(request):
    return HttpResponse("U are logged in!!!")


@login_required
def user_logout(request):
    logout(request)
    return render(request, 'basic_app/index.html', {})


def register(request):
    registered = False

    if request.method == "POST":
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():

            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']
            profile.save()
            registered = True
        else:
            print("Error")
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()
    return render(request, 'basic_app/register.html', {'user_form':user_form,  'profile_form':profile_form, 'registered': registered})


def user_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user is not None:
            return HttpResponseRedirect(reverse('index'))
        else:
            print("Credential Error")
            return HttpResponse("Invalid user id")

    else:
        return render(request, 'basic_app/login.html',)


