# Generated by Django 4.1 on 2022-08-15 03:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ExcelComp', '0015_alter_excelfiles_excfile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='user',
        ),
        migrations.RemoveField(
            model_name='file',
            name='owner',
        ),
        migrations.RemoveField(
            model_name='order',
            name='owner',
        ),
        migrations.RemoveField(
            model_name='order',
            name='processedfile',
        ),
        migrations.DeleteModel(
            name='Tag',
        ),
        migrations.DeleteModel(
            name='Customer',
        ),
        migrations.DeleteModel(
            name='File',
        ),
        migrations.DeleteModel(
            name='Order',
        ),
    ]
