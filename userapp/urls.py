from . import views
from django.urls import path

urlpatterns=[
    path('',views.index, name='index'),
    path('registeruserapp/',views.registeruser, name='registeruserapp'),
    path('loginpage/',views.loginpage, name='loginpage'),
    path('logout/',views.logout_page, name='logoutuser'),
    path('checkout/',views.checkout, name='checkout'),
    path('delete/<int:pk>',views.delete_booking, name='delete_booking'),
    path('booking/',views.booking, name='booking'),
    path('mytravel/',views.mytravels,name='mytravels'),
    path('confirm_booking/',views.confirm_booking,name='confirm_booking'),
    path('delete/<str:pk>',views.delete_booking, name='delete_booking'),
    path('update/<str:pk>',views.update, name='update'),
    path('succes/',views.succes, name='succes'),
    path('contact', views.contact_us, name="contact1"),
    # path('userapp/',views.index, name='user'),
    # path('accounts', views.login, name='login'),

    path('faredetails/',views.Fare, name='faredetails'),
    path('fare/',views.lipa_fare, name='fare'),
    path('access/token', views.getAccessToken, name='get_mpesa_access_token'),
    path('online/lipa', views.lipa_na_mpesa_online, name='lipa_na_mpesa'),
    path('c2b/register', views.register_urls, name="register_mpesa_validation"),
    path('c2b/confirmation', views.confirmation, name="confirmation"),
    path('c2b/validation', views.validation, name="validation"),
    path('c2b/callback', views.call_back, name="call_back"),
    path('about_us',views.about_us, name="about_us"),

    
] 
