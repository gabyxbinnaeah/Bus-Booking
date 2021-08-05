from django.contrib import admin
from .models import  Admin
from userapp.models import Book
from driverapp.models import Bus

admin.site.register(Admin)
admin.site.register(Bus)
admin.site.register(Book)