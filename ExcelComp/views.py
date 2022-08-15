
from importlib.metadata import requires
import re
from django.template import RequestContext
from csv import excel
from datetime import datetime
from distutils.command.upload import upload
from fileinput import filename
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
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
from .forms import *

# from . import twofilehighreturnone, twofileremovedupreturnone, onefilehighdup, onefileremovedup

# Date and Time to Add Uniqueness to the files
now = datetime.now()
dt_string = now.strftime("%d%m%Y%H%M%S")
dt_string2 = now.strftime("%d%m%Y%H%M%S%f")
dt_string3 = now.strftime("%d%m%Y%H%M")


# Create your views here.

@unauthenticated_user
def home(request):
    # orders = Order.objects.all()
    # customer = Customer.objects.all()
    return render(request, 'index.html')


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
    context = {}
    if request.method == 'POST':
        if 'deletedup' in request.POST:
            uploaded_files = request.FILES.getlist('file[]')
            i = 0
            fs = FileSystemStorage()
            for uploaded_file in uploaded_files:
                i += 1
                print(i)
                excel_file = fs.save(
                    (f"convert{i}{dt_string}.xlsx"), uploaded_file)

                # print(excel_file)
            convert2 = (f"ExcelComp/singlefiles/convert2{dt_string}.xlsx")
            convert1 = (f"ExcelComp/singlefiles/convert1{dt_string}.xlsx")

            # convert1 = fs.url(f"convert1{dt_string}.xlsx")
            # print(convert1, convert2)

            file_df1 = pd.read_excel(convert1)
            file_df2 = pd.read_excel(convert2)
            # print(file_df1)
            # print("Some Random Stuffss \n Stuffss Stuffss \n Stuffss Stuffss \n Stuffss Stuffss \n Stuffss Stuffss \n Stuffss Stuffss \n Stuffss Stuffss \n Stuffss   ")
            # print(file_df1)

            source_df = pd.concat([file_df1, file_df2])

            result_df = source_df.drop_duplicates()

            result_df.to_excel(
                f"ExcelComp/singlefiles/cleaned{dt_string2}.xlsx")

            dropname = (f"cleaned{dt_string2}.xlsx")
            context['url'] = fs.url(dropname)

        # ++====+++++ ====+++++++
        # Solution Here

        elif 'compare' in request.POST:
            uploaded_files = request.FILES.getlist('file[]')
            i = 0
            fs = FileSystemStorage()
            for uploaded_file in uploaded_files:
                i += 1
                # print(i)
                excel_file = fs.save(
                    (f"convert{i}{dt_string}.xlsx"), uploaded_file)

                # print(excel_file)
            convert2 = (f"ExcelComp/singlefiles/convert2{dt_string}.xlsx")
            convert1 = (f"ExcelComp/singlefiles/convert1{dt_string}.xlsx")

            # convert1 = fs.url(f"convert1{dt_string}.xlsx")
            # print(convert1, convert2)

            file_df1 = pd.read_excel(convert1)
            file_df2 = pd.read_excel(convert2)
            # print(file_df1)
            # print("Some Random Stuffss \n Stuffss Stuffss \n Stuffss Stuffss \n Stuffss Stuffss \n Stuffss Stuffss \n Stuffss Stuffss \n Stuffss Stuffss \n Stuffss   ")
            # print(file_df1)

            df2 = pd.concat([file_df1, file_df2])
            df2.to_excel(f'ExcelComp/singlefiles/{dt_string3}.xlsx')
            print
            excel_file = f'ExcelComp/singlefiles/{dt_string3}.xlsx'
            # excel_file = 'excel1.xlsx'

            file_df = pd.read_excel(excel_file)

            df = pd.DataFrame(file_df)

            del df[df.columns[0]]

            # print(df)

            df.loc[df.duplicated(keep=False), :]
            # df.loc[df.duplicated(keep=False), :]

            hello = df.loc[df.duplicated(keep=False), :]
            # print(hello)
            keyword1 = df.columns[0]
            keyword2 = hello.columns[0]

            duplicated = df[keyword1].isin(hello[keyword2])

            def row_styler(row):
                return ['background-color: yellow' if duplicated[row.name] else ''] * len(row)

            df.style.apply(row_styler, axis=1)

            result_df = df.style.apply(row_styler, axis=1)

            result_df.to_excel(
                f"ExcelComp/singlefiles/Highlighted{dt_string2}.xlsx")

            dropname = (f"Highlighted{dt_string2}.xlsx")
            context['url'] = fs.url(dropname)
        elif 'deletedup2' in request.POST:
            uploaded_files = request.FILES.getlist('file[]')
            i = 0
            fs = FileSystemStorage()
            for uploaded_file in uploaded_files:
                i += 1
                print(i)
                excel_file = fs.save(
                    (f"convert{i}{dt_string}.xlsx"), uploaded_file)

                # print(excel_file)
            convert2 = (f"ExcelComp/singlefiles/convert2{dt_string}.xlsx")
            convert1 = (f"ExcelComp/singlefiles/convert1{dt_string}.xlsx")

            # convert1 = fs.url(f"convert1{dt_string}.xlsx")
            # print(convert1, convert2)

            file_df1 = pd.read_excel(convert1)
            file_df2 = pd.read_excel(convert2)
            # print(file_df1)
            # print("Some Random Stuffss \n Stuffss Stuffss \n Stuffss Stuffs \n Stuffss Stuffss \n Stuffss Stuffss \n Stuffss Stuffss \n Stuffss Stuffss \n Stuffss   ")
            # print(file_df1)

            source_df = pd.concat([file_df1, file_df2])

            result_df = source_df.drop_duplicates()
            result_df2 = source_df.loc[source_df.duplicated(), :]
            result_df.to_excel(
                f"ExcelComp/singlefiles/cleaned{dt_string2}.xlsx")
            result_df2.to_excel(
                f"ExcelComp/singlefiles/RemovedDups{dt_string2}.xlsx")

            dropname = (f"cleaned{dt_string2}.xlsx")
            dropname2 = (f"RemovedDups{dt_string2}.xlsx")
            context['url'] = fs.url(dropname)
            context['url2'] = fs.url(dropname2)

        # ++====+++++ ====+++++++
        # Solution Here

        elif 'compare2' in request.POST:
            uploaded_files = request.FILES.getlist('file[]')
            i = 0
            fs = FileSystemStorage()
            for uploaded_file in uploaded_files:
                i += 1
                # print(i)
                excel_file = fs.save(
                    (f"convert{i}{dt_string}.xlsx"), uploaded_file)

                # print(excel_file)
            convert2 = (f"ExcelComp/singlefiles/convert2{dt_string}.xlsx")
            convert1 = (f"ExcelComp/singlefiles/convert1{dt_string}.xlsx")

            # convert1 = fs.url(f"convert1{dt_string}.xlsx")
            # print(convert1, convert2)

            file_df1 = pd.read_excel(convert1)
            file_df2 = pd.read_excel(convert2)

            keyword1 = file_df1.columns[0]
            keyword2 = file_df2.columns[0]

            duplicated1 = file_df1[keyword1].isin(file_df2[keyword2])
            duplicated2 = file_df2[keyword2].isin(file_df1[keyword1])

            def row_styler(row):

                return ['background-color: yellow' if duplicated1[row.name] else ''] * len(row)

            def row_styler2(row):

                return ['background-color: yellow' if duplicated2[row.name] else ''] * len(row)

            exceloutput1 = file_df1.style.apply(row_styler, axis=1)
            exceloutput2 = file_df2.style.apply(row_styler2, axis=1)

            exceloutput1.to_excel(
                f"ExcelComp/singlefiles/File1{dt_string2}.xlsx")
            exceloutput2.to_excel(
                f"ExcelComp/singlefiles/File2{dt_string2}.xlsx")

            dropname = (f"File1{dt_string2}.xlsx")
            dropname2 = (f"File2{dt_string2}.xlsx")
            context['url'] = fs.url(dropname)
            context['url2'] = fs.url(dropname2)
    return render(request, 'multipleFiles.html', context)


@ login_required(login_url='login')
def singlefile(request):
    context = {}
    if request.method == 'POST':
        if 'deletedup' in request.POST:
            uploaded_file = request.FILES['singlefile']
            fs = FileSystemStorage()
            # fs.save(uploaded_file.name, uploaded_file)
            # print(fs.url(uploaded_file.name, uploaded_file))
            # fs.url(name)
            excel_file = uploaded_file
            # print(excel_file)

            file_df = pd.read_excel(excel_file)
            source_df = pd.DataFrame(file_df)
            # print('Source DataFrame:\n', source_df)
            result_df = source_df.drop_duplicates()
            # print('Result DataFrame:\n', result_df)
            result_df.to_excel(
                f"ExcelComp/singlefiles/cleaned{dt_string + uploaded_file.name}.xlsx")
            dropname = (
                f"cleaned{dt_string + uploaded_file.name}.xlsx")
            context['url'] = fs.url(dropname)
        elif 'compare' in request.POST:
            uploaded_file = request.FILES['singlefile']
            fs = FileSystemStorage()
            # fs.save(uploaded_file.name, uploaded_file)
            # fs.url(name)
            excel_file = uploaded_file
            file_df = pd.read_excel(excel_file)
            df2 = pd.DataFrame(file_df)

            df2.loc[df2.duplicated(keep=False), :]

            hello = df2.loc[df2.duplicated(keep=False), :]

            keyword1 = df2.columns[0]
            keyword2 = hello.columns[0]

            duplicated = df2[keyword1].isin(hello[keyword2])

            def row_styler(row):
                return ['background-color: yellow' if duplicated[row.name] else ''] * len(row)

            df2.style.apply(row_styler, axis=1)
            result_df2 = df2.style.apply(row_styler, axis=1)
            result_df2.to_excel(
                f"ExcelComp/singlefiles/compare{dt_string + uploaded_file.name}.xlsx")
            dropname = (
                f"compare{dt_string + uploaded_file.name}.xlsx")
            context['url'] = fs.url(dropname)
        if 'deletedup1' in request.POST:
            uploaded_file = request.FILES['singlefile']
            fs = FileSystemStorage()
            # fs.save(uploaded_file.name, uploaded_file)

            source_df0 = uploaded_file
            file_df = pd.read_excel(source_df0)

            source_df = pd.DataFrame(file_df)

            # print(file_df1)
            # print("Some Random Stuffss \n Stuffss Stuffss \n Stuffss Stuffs \n Stuffss Stuffss \n Stuffss Stuffss \n Stuffss Stuffss \n Stuffss Stuffss \n Stuffss   ")
            # print(file_df1)

            result_df = source_df.drop_duplicates()
            result_df2 = source_df.loc[source_df.duplicated(), :]

            result_df.to_excel(
                f"ExcelComp/singlefiles/cleaned{dt_string2}.xlsx")
            result_df2.to_excel(
                f"ExcelComp/singlefiles/RemovedDups{dt_string2}.xlsx")

            dropname = (f"cleaned{dt_string2}.xlsx")
            dropname2 = (f"RemovedDups{dt_string2}.xlsx")
            context['url'] = fs.url(dropname)
            context['url2'] = fs.url(dropname2)
    return render(request, 'singlefile.html', context)


@ login_required(login_url='login')
def convert(request):
    context = {}
    if request.method == 'POST':
        if 'convert' in request.POST:
            uploaded_file = request.FILES['singlefile']
            fs = FileSystemStorage()
            # fs.save(uploaded_file.name, uploaded_file)

            excel_file = uploaded_file

            file_df = pd.read_excel(excel_file)

            file_df.to_html(
                f"ExcelComp/singlefiles/convert{dt_string + uploaded_file.name}.html")
            dropname = (
                f"convert{dt_string + uploaded_file.name}.html")
            context['url'] = fs.url(dropname)

    return render(request, 'convert.html', context)


def customer(request):
    owner = request.user
    form = ExcelFileForm()
    if request.method == 'POST':
        form = ExcelFileForm(request.POST, request.FILES)
        file = request.FILES["excfile"]
        excelfi = ExcelFiles.objects.create(excfile=file)
        excelfi.save()
        return HttpResponse(f"The {excelfi.pk} has {excelfi.excfile} ")
        # ExcelFileForm.owner = owner
        # owner = request.user['user']

        if form.is_valid():
            form.save()
            return HttpResponse(f"Owner is{excfile} and user is")
        # return redirect('customer')

    return render(request, 'profile.html', {"form": form})


def contact(request):
    context = {}
    form = FeedbackForm()
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request, 'Form Submitted Successful, You Will Hear From Us')
            return redirect('contact')

    return render(request, 'contact.html', context)


def faq(request):
    return render(request, 'faq.html')


def terms(request):
    return render(request, 'tc.html')


@ login_required(login_url='login')
def dashboard(request):
    return render(request, 'dashboard.html')


def aboutus(request):
    return render(request, 'aboutus.html')


# def terms(request):
#     return render(request, 'tc.html')
# def terms(request):
#     return render(request, 'tc.html')


def handler404(request):
    return render(request, '404.html', status=404)


def handler500(request):
    return render(request, '500.html', status=500)


def mission(request):
    return render(request, 'mission.html')


@ login_required(login_url='login')
def featureselect(request):
    return render(request, 'featureselect.html')


# @ login_required(login_url='login')
# def customer(request):

#     return render(request, 'profile.html')


@login_required(login_url='login')
def library(request):
    # Add all view from the files in the Library
    return render(request, 'library.html')


@login_required(login_url='login')
def libgrid(request):
    # Add all view from the files in the Library
    return render(request, 'librarygrid.html')


def error_404(request, exception):
    data = {}
    return render(request, '404.html', data)


def error_500(request):
    data = {}
    return render(request, '404.html', data)


def error_400(request, exception):
    data = {}
    return render(request, '404.html', data)


def error_403(request,  exception):
    data = {}
    return render(request, '404.html', data)
