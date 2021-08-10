from django.urls import path
from . import views
from django.conf.urls import url

urlpatterns=[
    path('',views.home, name='drivers_dash'),
    path('busses-dash/',views.busses, name='busses-dash'),
    url(r'^register/$', views.registerDriver, name="driverregister"),
    url(r'^loginpage/$', views.loginPage, name="driverlogin"), 
    url(r'^logout/$',views.logoutDriver,name="logout"),
   
    path('create_order/', views.create_driver, name="create_order"),
    path('update_order/<str:pk>/', views.update_driver, name="update_order"),
    path('driver/<str:pk_test>/', views.driver, name="driver"),
    path('bus/<str:pk_test>/', views.driver, name="bus"),
    path('delete_order/<str:pk>/', views.delete_driver, name="delete_order"),
    path('create_order_bus/', views.add_bus, name="create_order_bus"),
    path('update_order_bus/<str:pk>/', views.update_bus, name="update_order_bus"),
    path('delete_order_bus/<str:pk>/', views.delete_bus, name="delete_order_bus"),

]