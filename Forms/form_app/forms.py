from django import forms
from django.core import validators


class UserInfo(forms.Form):
    name = forms.CharField(max_length=264)
    email = forms.EmailField(max_length=264)
    verify_email = forms.EmailField(label="Enter your Email again")
    text = forms.CharField(widget=forms.Textarea)



    def clean(self):
        all_clean_data = super().clean()
        email = all_clean_data['email']
        vemail = all_clean_data['verify_email']


        if(email != vemail):
            raise forms.ValidationError('Email Does not match')
