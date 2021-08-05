from django.urls import path
from . import views
from django.conf.urls import url

urlpatterns=[
    path('',views.index, name='index'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('customer/',views.customer, name='customer'),
    path('registeruser/',views.registeruser, name='register'),
    path('loginpage/',views.loginpage, name='loginpage'),     
    path('driverapp/',views.index, name='driverapp'),
]