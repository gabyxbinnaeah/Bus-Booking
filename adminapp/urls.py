from django.urls import path
from . import views
from django.conf.urls import url

urlpatterns=[
    path('',views.index, name='passengers-dash'),
    path('busses/',views.busses, name='busses-dash'),
    # url(r'^$',views.admin, name='admin'),
    # url(r'^login/$', views.loginPage, name="adminlogin"), 
    url(r'^logout/$',views.logoutUser,name="logout"),
    url(r'^contact/$',views.contact,name="contact"),

    path('busses-dash/',views.busses, name='buses-dash'),
    path('adminregister/', views.registerAdmin, name='adminregister'),
    path('superapplogin/', views.loginPage, name='superapplogin'), 
    path('logout/',views.logoutUser,name='logout'),
    path('contact/',views.contact,name='contact'),
    path('create_order/', views.create_pass, name="create_order_pass"),
    path('update_order/<str:pk>/', views.update_pass, name="update_order_pass"),
    path('passenger/<str:pk_test>/', views.passenger, name="passenger"),
    path('bus/<str:pk_test>/', views.driver, name="bus-"),
    path('delete_order/<str:pk>/', views.delete_pass, name="delete_order_pass"),
    path('create_order_bus/', views.create_bus, name="create_order_bus-"),
    path('update_order_bus/<str:pk>/', views.update_bus, name="update_order_bus-"),
    path('delete_order_bus/<str:pk>/', views.delete_bus, name="delete_order_bus-"),
    # url(r'admin/',views.admin, name='admin'),
    # url(r'^register/$', views.registerPage, name="adminregister"),
#    path('profile/', views.profile, name='profile'),
    path('driver/',views.driver_details, name='driver-dash'),
   
   

]
