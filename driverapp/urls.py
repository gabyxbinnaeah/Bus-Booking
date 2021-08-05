from django.urls import path
from . import views
from django.conf.urls import url

urlpatterns=[
    path('index',views.index, name='index'),
    path('customer/',views.customer, name='customer'),
    path('registeruser/',views.registeruser, name='register'),
    path('loginpage/',views.loginpage, name='loginpage'), 
     path('', views.dashboard, name='dashboard'),    
]