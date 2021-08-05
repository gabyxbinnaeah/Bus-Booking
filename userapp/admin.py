from django.contrib import admin

# Register your models here.
from .models import *

# Register your models here.
admin.site.register(Bus)

admin.site.register(Book)

admin.site.register(BusCategory)
