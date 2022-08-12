from datetime import datetime
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from django.core.files.storage import FileSystemStorage
from django.conf.urls.static import static
from .decorator import *
from .models import *
from .forms import CreateUserForm

# Date and Time to Add Uniqueness to the files
now = datetime.now()
dt_string = now.strftime("%d%m%Y%H%M%S")


# Create your views here.


def home(request):
    # orders = Order.objects.all()
    # customer = Customer.objects.all()
    return render(request, 'index.html')


def contact(request):
    return render(request, 'contact.html')


@login_required(login_url='login')
def library(request):
    # Add all view from the files in the Library
    return render(request, 'library.html')


@login_required(login_url='login')
def libgrid(request):
    # Add all view from the files in the Library
    return render(request, 'librarygrid.html')


@unauthenticated_user
def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.info(request, 'Username OR password is incorrect')

    context = {}
    return render(request, 'login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('login')


@unauthenticated_user
def signup(request):

    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for ' + user)

            return redirect('login')

    context = {'form': form}
    return render(request, 'signup.html', context)


@login_required(login_url='login')
def multifiles(request):
    return render(request, 'multipleFiles.html')


@login_required(login_url='login')
def singlefile(request):
    context = {}
    if request.method == 'POST':
        uploaded_file = request.FILES['singlefile']
        fs = FileSystemStorage()
        fs.save(uploaded_file.name, uploaded_file)
        # fs.url(name)
        excel_file = uploaded_file

        file_df = pd.read_excel(excel_file)
        source_df = pd.DataFrame(file_df)
        print('Source DataFrame:\n', source_df)
        result_df = source_df.drop_duplicates()
        print('Result DataFrame:\n', result_df)
        result_df.to_excel(
            f"ExcelComp/singlefiles/{dt_string + uploaded_file.name}.xlsx")
        dropname = (
            f"{dt_string + uploaded_file.name}.xlsx")
        context['url'] = fs.url(dropname)
    return render(request, 'singlefile.html', context)


def terms(request):
    return render(request, 'tc.html')


@login_required(login_url='login')
def dashboard(request):
    return render(request, 'dashboard.html')


@login_required(login_url='login')
def featureselect(request):
    return render(request, 'featureselect.html')


@login_required(login_url='login')
def customer(request):
    # customer = Customer.object.all()
    context = {}
    context = {'customer': customer}
    return render(request, 'profile.html')
