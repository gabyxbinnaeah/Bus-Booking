from . import views
from django.urls import path

urlpatterns=[
    path('',views.index, name='index'),
    path('registeruser/',views.registeruser, name='register'),
    path('loginpage/',views.loginpage, name='loginpage'),



]