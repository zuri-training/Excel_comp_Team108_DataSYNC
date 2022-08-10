
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegisterForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import logout

from rest_framework import viewsets
 
# import local data
from .models import Profile
 
# Create your views here.

def home(request):
    return render(request, 'users/home.html')


def register(request):
    
    if request.user.is_authenticated:
        return redirect('/')
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, f'Hi {username}, your account was created successfully')
            return redirect('home')
        else:
            return render(request, 'users/register.html', {'form': form})
    else:
        form = UserRegisterForm()

    return render(request, 'users/register.html', {'form': form})


def login(request):
    if request.user.is_authenticated:
        return render(request, 'users/home.html')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            form = AuthenticationForm(request.POST)
            return render(request, 'users/login.html', {'form': form})
    else:
        form = AuthenticationForm()
        return render(request, 'users/login.html', {'form': form})


@login_required()
def profile(request):
    return render(request, 'users/profile.html')


   
def signout(request):
    logout(request)
    return redirect('/')

