# Generated by Django 3.1 on 2021-08-05 19:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0002_auto_20210805_0926'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='dest',
            new_name='destination',
        ),
    ]
