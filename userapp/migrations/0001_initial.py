# Generated by Django 3.1.7 on 2021-08-12 12:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import multiselectfield.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('adminapp', '__first__'),
        ('driverapp', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('name', models.CharField(max_length=30)),
                ('source', models.CharField(max_length=30)),
                ('destination', models.CharField(blank=True, max_length=30, null=True)),
                ('fare', models.CharField(max_length=6, null=True)),
                ('date', models.DateField(null=True)),
                ('time', models.TimeField(null=True)),
                ('status', models.CharField(choices=[('B', 'Booked'), ('C', 'Cancelled')], default='B', max_length=2)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('seat_no', multiselectfield.db.fields.MultiSelectField(choices=[(1, '1'), (2, '2'), (4, '4'), (5, '5'), (6, '6'), (7, '7'), (8, '8'), (9, '9'), (10, '10'), (11, '11'), (12, '12'), (13, '13'), (14, '14'), (15, '15'), (16, '16'), (17, '17'), (18, '18'), (19, '19'), (20, '20'), (21, '21'), (22, '22'), (23, '23'), (24, '24'), (25, '25')], max_length=200, null=True)),
                ('checked_seats', models.CharField(max_length=2)),
                ('admin_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='admin', to='adminapp.admin')),
                ('busid', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='driverapp.bus')),
                ('userid', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
