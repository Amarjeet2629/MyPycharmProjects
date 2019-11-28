from django import forms
from .models import UserInfo
from django.contrib.auth.models import User


class UserSignUpForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    email = forms.EmailField(required=True)

    class Meta():
        model = User
      #  password = forms.PasswordInput()
        fields = ('first_name', 'last_name', 'username', 'password', 'email')

