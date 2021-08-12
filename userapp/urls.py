from . import views
from django.urls import path

urlpatterns=[
    path('',views.index, name='index'),
    path('booking/<id>', views.booking, name='booking'),
    path('registeruser/',views.registeruser, name='register'),
    path('loginpage/',views.loginpage, name='loginpage'),
    path('logout/',views.logout_page, name='logout'),
    path('checkout/',views.checkout, name='checkout'),
    path('aboutus/',views.aboutus, name='aboutus'),
    path('delete/<int:pk>',views.delete_booking, name='delete_booking'),
    path('contact_us/',views.contact_us, name='contact_us'),
]