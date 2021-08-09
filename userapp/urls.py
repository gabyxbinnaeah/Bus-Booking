from . import views
from django.urls import path

urlpatterns=[
    path('',views.index, name='index'),
    path('accounts', views.login, name='login'),
    path('seats/', views.seats, name='seats'),

    path('test/', views.test, name='test'),

    path('home/',views.index, name='index'),
    path('booking/',views.booking,name='booking'),
    path('confirm_booking/',views.confirm_booking,name='confirm_booking'),
]