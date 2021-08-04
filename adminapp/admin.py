from django.contrib import admin
from .models import Bus, Book, Admin

admin.site.register(Admin)
admin.site.register(Bus)
admin.site.register(Book)