from django.contrib import admin
from .models import Book

from .models import *

# Register your models here.

admin.site.register(Bus)

admin.site.register(Book)

admin.site.register(BusCategory)
