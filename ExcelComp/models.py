
from django.db import models
import pandas as pd

# Create your models here.


class ContactUs(models.Model):
    name = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    message = models.TextField(max_length=3000, null=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Customer(models.Model):
    name = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name


class File(models.Model):
    EXCELTYPE = (
        ('CSV', 'CSV'),
        ('XLSX', 'XLSX'),
        ('PDF', 'PDF'),
    )
    name = models.CharField(max_length=200, null=True)
    description = models.CharField(max_length=200, null=True)
    status = models.CharField(max_length=200, null=True, choices=EXCELTYPE)
    date_created = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(Customer, null=True, on_delete=models.SET_NULL)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.name


class Order(models.Model):
    STATUS = (
        ('Pending', 'Pending'),
        ('Converted', 'Converted'),
        ('Compared', 'Compared'),
    )
    processedfile = models.ForeignKey(
        File, null=True, on_delete=models.SET_NULL)
    owner = models.ForeignKey(Customer, null=True, on_delete=models.SET_NULL)
    date_created = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=200, null=True, choices=STATUS)


# class single_File_Duplicate():
#     excel_file = '{{ url }}'
#     file_df = pd.read_excel(excel_file)
#     source_df = pd.DataFrame(file_df)
#     print('Source DataFrame:\n', source_df)
#     result_df = source_df.drop_duplicates()
#     print('Result DataFrame:\n', result_df)
#     result_df.to_excel("my_excel_file.xlsx")


# class Removeduplicate():

#     workbook = pd.read_excel(r'')

#     workbook.drop_duplicates()

#     def __str__(self):
#         return self.workbook
