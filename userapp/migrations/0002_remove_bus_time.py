# Generated by Django 3.1.7 on 2021-08-04 21:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bus',
            name='time',
        ),
    ]
