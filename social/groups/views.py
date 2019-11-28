from django.shortcuts import render

# Create your views here.

from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

from django.urls import reverse
from django.views.generic import CreateView, ListView, DetailView
from .models import Group, GroupMember


class CreateGroup(CreateView, LoginRequiredMixin):
    model = Group
    fields = ('name', 'description')


class SingleGroup(DetailView):
    model = Group


class ListGroups(ListView):
    model = Group
