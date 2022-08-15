from django.contrib import admin
from .models import *
# Register your models here.


admin.site.register(ExcelFiles)
admin.site.register(ProcessedFiles)

admin.site.register(Feedback)
