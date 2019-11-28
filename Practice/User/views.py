from django.shortcuts import render
from django.http import HttpResponse
from .models import user
from .forms import NewUser
# Create your views here.


def start(request):
    return render(request, 'User/SignUp.html', {})


def index(request):
    form = NewUser()

    if request.method == 'POST':
        form = NewUser(request.POST)

        if form.is_valid():

            return start(request)
        else:
            print("Error form invalid")
    return render(request, 'User/SignUp.html', {'form': form})