
from django.db import models

# Create your models here.


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
