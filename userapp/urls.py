from django.urls import path
from . import views
from django.conf.urls import url

urlpatterns=[
    path('',views.index, name='index'),
    path('accounts', views.login, name='login'),
    path('seats', views.seats, name='seats'),


    path('user/',views.index, name='index'),
]