from django.contrib import admin
from .models import *
# Register your models here.
from import_export.admin import ImportExportModelAdmin

admin.site.register(Customer)
# admin.site.register(File)
admin.site.register(Order)
admin.site.register(Tag)


@admin.register(File)
class userdat(ImportExportModelAdmin):
    pass
