from . import views
from django.urls import path

urlpatterns=[
    # path('userapp/',views.index, name='user'),
    path('userapp/',views.index, name='index'),
    path('accounts', views.login, name='login'),
    path('seats', views.seats, name='seats'),
    
]
