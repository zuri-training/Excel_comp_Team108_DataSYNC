from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory
from .models import *

# Create your views here.


def terms(HttpResponse):
    return HttpResponse('Hello World')
