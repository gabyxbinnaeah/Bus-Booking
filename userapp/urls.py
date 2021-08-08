from . import views
from django.urls import path

urlpatterns=[
    path('home/',views.index, name='index'),
    path('booking/',views.booking,name='booking'),
    path('confirm_booking/',views.confirm_booking,name='confirm_booking'),
]