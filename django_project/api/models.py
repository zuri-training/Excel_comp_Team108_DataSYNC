from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.utils import timezone
import datetime
from .managers import CustomUserManager

# Create your models here.


class User(AbstractBaseUser, PermissionsMixin):

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'
        db_table = 'user'
    id = models.AutoField(primary_key=True)
    email = models.EmailField(max_length=100, unique=True)
    first_name = models.CharField(max_length = 100, null = True, blank = True)
    last_name = models.CharField(max_length = 100, null = True, blank = True)
    date_joined = models.DateTimeField(auto_now_add=True)
    modified_date = models.CharField(max_length=30, blank=True)
    is_active   = models.BooleanField(default = True)
    is_staff   = models.BooleanField(default = True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email
