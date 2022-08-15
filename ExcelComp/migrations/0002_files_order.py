# Generated by Django 4.1 on 2022-08-11 00:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ExcelComp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Files',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('description', models.CharField(max_length=200, null=True)),
                ('status', models.CharField(choices=[('CSV', 'CSV'), ('XLSX', 'XLSX'), ('PDF', 'PDF')], max_length=200, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('Converted', 'Converted'), ('Compared', 'Compared')], max_length=200, null=True)),
            ],
        ),
    ]