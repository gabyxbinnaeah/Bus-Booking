# Generated by Django 3.1.7 on 2021-08-04 19:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bus_name', models.CharField(max_length=30)),
                ('source', models.CharField(max_length=30)),
                ('dest', models.CharField(max_length=30)),
                ('nos', models.IntegerField(default=0)),
                ('rem', models.CharField(max_length=5, null=True)),
                ('fare', models.CharField(max_length=6, null=True)),
                ('date', models.DateField()),
                ('time', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('name', models.CharField(max_length=30)),
                ('source', models.CharField(max_length=30)),
                ('dest', models.CharField(blank=True, max_length=30, null=True)),
                ('seat_no', models.CharField(max_length=30, null=True)),
                ('fare', models.CharField(max_length=6, null=True)),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('status', models.CharField(choices=[('B', 'Booked'), ('C', 'Cancelled')], default='B', max_length=2)),
                ('busid', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='userapp.bus')),
                ('userid', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='userapp.user')),
            ],
        ),
    ]
