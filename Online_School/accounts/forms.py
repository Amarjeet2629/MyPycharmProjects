from django import forms
from django.contrib.auth.models import User
from .models import TeacherProfileInfo, StudentProfileInfo
from django.contrib.auth.password_validation import validate_password
from django.core import validators


class StudentSignUpForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(), validators=[validate_password])

    class Meta:
        model = User
        fields = ('username', 'password', 'email', 'first_name', 'last_name')


class TeacherSignUpForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(), validators=[validate_password])

    class Meta:
        model = User
        fields = ('username', 'password', 'email', 'first_name', 'last_name')


class TeacherProfilePicForm(forms.ModelForm):
    class Meta:
        model = TeacherProfileInfo
        fields = ('profile_pic', )


class StudentProfilePicForm(forms.ModelForm):
    class Meta:
        model = StudentProfileInfo
        fields = ('profile_pic', )
