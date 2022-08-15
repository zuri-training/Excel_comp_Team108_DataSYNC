

from django.db import models
import pandas as pd
from django.contrib.auth.models import User
# Create your models here.


class Feedback(models.Model):
    feedname = models.CharField(max_length=200, null=True)
    feedmail = models.CharField(max_length=200, null=True)
    feedmsg = models.TextField(max_length=3000, null=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.feedname


class ExcelFiles(models.Model):
    excfile = models.FileField(null=True)
    owner = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.owner


class ProcessedFiles(models.Model):

    file1 = models.CharField(max_length=200, null=True)
    owner = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.feedname
