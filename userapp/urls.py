from . import views
from django.urls import path

urlpatterns=[
    path('',views.search_bus, name='index'),
    path('registeruser/',views.registeruser, name='register'),
    path('loginpage/',views.loginpage, name='loginpage'),
    path('logout/',views.logout_page, name='logout'),
    path('checkout/',views.checkout, name='checkout'),
    path('delete/<int:pk>',views.delete_booking, name='delete_booking'),
    path('booking/',views.booking, name='booking'),

    # path('userapp/',views.index, name='user'),
    path('userapp/',views.index, name='index'),
    path('accounts', views.login, name='login'),
    path('seats', views.seats, name='seats'),
    
] 
