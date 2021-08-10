from . import views
from django.urls import path

urlpatterns=[
    path('',views.index, name='index'),
    path('registeruser/',views.registeruser, name='register'),
    path('loginpage/',views.loginpage, name='loginpage'),
    path('logout/',views.logout_page, name='logout'),
    path('checkout/',views.checkout, name='checkout'),
    path('delete/<int:pk>',views.delete_booking, name='delete_booking'),
    path('booking/',views.booking, name='booking'),


    path('mytravel/',views.mytravels,name='mytravels'),

    path('confirm_booking/',views.confirm_booking,name='confirm_booking'),

]