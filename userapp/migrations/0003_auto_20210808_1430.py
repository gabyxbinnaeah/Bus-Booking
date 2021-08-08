# Generated by Django 3.1.7 on 2021-08-08 11:30

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0002_auto_20210808_1425'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='seat_no',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('green', 'GREEN'), ('blue', 'BLUE'), ('red', 'RED'), ('orange', 'ORANGE'), ('black', 'BLACK')], max_length=30, null=True),
        ),
    ]
