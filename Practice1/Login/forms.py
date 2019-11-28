from django import forms
from Login.models import user


class NewUser(forms.ModelForm):
    class Meta():
        model = user
        fields = '__all__'
