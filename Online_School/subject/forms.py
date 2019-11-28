from django import forms
from .models import Course
from django.contrib.auth.models import User


class CourseCreateForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ('name', 'description')

