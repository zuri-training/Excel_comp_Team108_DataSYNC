# Generated by Django 4.1 on 2022-08-15 11:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ExcelComp', '0017_processedfiles'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='processedfiles',
            name='file2',
        ),
    ]