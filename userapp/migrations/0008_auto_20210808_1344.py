# Generated by Django 3.1.7 on 2021-08-08 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0007_auto_20210808_1336'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='time',
            field=models.TimeField(null=True),
        ),
    ]
