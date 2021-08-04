from django.urls import path
from . import views

urlpatterns=[
    path('driverapp/',views.index, name='driverapp'),
]