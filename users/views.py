from django.shortcuts import render
from users.models import User

# Create your views here.


def registration(request):
    return render(request, 'users/registration.html')


def login(request):
    return render(request, 'users/login.html')