from django import forms
from . import models
from .models import user


class NewUser(forms.ModelForm):
    class Meta():
        model = user
        fields = "__all__"
