from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import *


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class FeedbackForm(ModelForm):
    class Meta:
        model = Feedback
        fields = '__all__'


class ExcelFileForm(ModelForm):
    class Meta:
        model = ExcelFiles
        exclude = ('owner',)
        fields = '__all__'


class ProcessedDoc(ModelForm):
    class Meta:
        model = ProcessedFiles
        fields = '__all__'
