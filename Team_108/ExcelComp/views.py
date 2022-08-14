from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required


from .models import *
from .forms import CreateUserForm

# Create your views here.


def home(request):
    # orders = Order.objects.all()
    # customer = Customer.objects.all()
    return render(request, 'ExcelComp/index.html')


def contact(request):
    return render(request, 'ExcelComp/contact.html')


@login_required(login_url='login')
def library(request):
    # Add all view from the files in the Library
    return render(request, 'ExcelComp/library.html')


def loginPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.info(request, 'Username OR password is incorrect')

    context = {}
    return render(request, 'ExcelComp/login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('login')


def signup(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account was created for ' + user)

                return redirect('login')

        context = {'form': form}
        return render(request, 'ExcelComp/signup.html', context)


@login_required(login_url='login')
def multifiles(request):
    return render(request, 'ExcelComp/multipleFiles.html')


@login_required(login_url='login')
def singlefile(request):
    return render(request, 'ExcelComp/singlefile.html')


def terms(request):
    return render(request, 'ExcelComp/tc.html')


@login_required(login_url='login')
def customer(request):
    customer = Customer.object.all()

    context = {'customer': customer}
    return render(request, 'ExcelComp/profile.html')
