# Generated by Django 3.1.7 on 2021-08-05 21:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('driverapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bus',
            old_name='dest',
            new_name='destination',
        ),
        migrations.RenameField(
            model_name='bus',
            old_name='nos',
            new_name='number_of_Seats',
        ),
        migrations.RemoveField(
            model_name='bus',
            name='rem',
        ),
    ]