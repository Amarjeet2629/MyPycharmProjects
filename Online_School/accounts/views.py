from django.shortcuts import render
from .models import StudentProfileInfo, TeacherProfileInfo
from .forms import StudentProfilePicForm, TeacherProfilePicForm, TeacherSignUpForm, StudentSignUpForm
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import reverse
from django.contrib.auth import login, logout, authenticate
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
# Create your views here.



def StudentSignUp(request):
    registered = False
    if request.method == 'POST':
        sign_up_form = StudentSignUpForm(request.POST, request.FILES)
        profile_pic_form = StudentProfilePicForm(request.POST, request.FILES)

        if sign_up_form.is_valid() and profile_pic_form.is_valid():
            user_sign_up = sign_up_form.save(commit=False)
            user_sign_up.set_password(user_sign_up.password)
            user_sign_up.save()
            profile_pic1 = profile_pic_form.save(commit=False)
            profile_pic1.user = user_sign_up
            if request.FILES.get('profile_pic'):
                profile_pic1.profile_pic = request.FILES['profile_pic']
            profile_pic1.save()
            registered = True
            return HttpResponseRedirect(reverse('homepage'))
        else:
            print(sign_up_form.errors, profile_pic_form.errors)
            return HttpResponse("fucked up")
    else :
        sign_up_form = StudentSignUpForm()
        profile_pic_form = StudentProfilePicForm()
        return render(request, 'accounts/student_sign_up.html', {'sign_up_form': sign_up_form, 'profile_pic_form': profile_pic_form, 'registered': registered })


def TeacherSignUp(request):
    registered = False
    if request.method == 'POST':
        sign_up_form = TeacherSignUpForm(request.POST)
        profile_pic_form = TeacherProfilePicForm(request.FILES)
        if sign_up_form.is_valid() and profile_pic_form.is_valid():
            user_sign_up = sign_up_form.save(commit=False)
            user_sign_up.set_password(user_sign_up.password)
            user_sign_up.save()
            profile_pic1 = profile_pic_form.save(commit=False)
            profile_pic1.user = user_sign_up
            if request.FILES.get('profile_pic'):
                profile_pic1.profile_pic = request.FILES['profile_pic']
            profile_pic1.save()
            registered = True
            return HttpResponseRedirect(reverse('homepage'))
        else:
            print(sign_up_form.errors, profile_pic_form.errors)
            return HttpResponse("fucked up")
    else:
        sign_up_form = StudentSignUpForm()
        profile_pic_form = StudentProfilePicForm()
        return render(request, 'accounts/teacher_sign_up.html',
                      {'sign_up_form': sign_up_form, 'profile_pic_form': profile_pic_form, 'registered': registered})


def UserLogin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('accounts:profile_single', kwargs={'username': username}))
            else:
                return HttpResponse('You are not active try contacting the admin')
        else:
            raise ValueError(username, password)
    else:
        return render(request, 'accounts/login.html', {})

@login_required
def ProfileSingle(request, username):
    obj1 = StudentProfileInfo.objects.filter(user=request.user).exists()
    obj2 = TeacherProfileInfo.objects.filter(user=request.user).exists()
    if obj1:
        obj1 = StudentProfileInfo.objects.get(user=request.user)
        return render(request, 'accounts/profile_detail.html', {'obj': obj1})
    else:
        obj2 = TeacherProfileInfo.objects.get(user=request.user)
        return render(request, 'accounts/profile_detail.html', {'obj': obj2})

