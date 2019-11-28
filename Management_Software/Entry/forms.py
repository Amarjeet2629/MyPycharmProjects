from django import forms
from .models import Host, Visitor


class HostRegisterForm(forms.ModelForm):
    class Meta:
        model = Host
        fields = ('name', 'email', 'phone_number')


class VisitorRegisterForm(forms.ModelForm):
    class Meta:
        model = Visitor
        fields = ('name', 'email', 'phone_number', 'host_name', 'checkin_time', 'checkout_time')
