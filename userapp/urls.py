from . import views
from django.urls import path

urlpatterns=[
    path('',views.index, name='index'),
    path('accounts', views.login, name='login'),
    path('seats/', views.seats, name='seats'),

    path('test/', views.test, name='test'),

]