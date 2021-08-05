from django.urls import path
from . import views
from django.conf.urls import url

urlpatterns=[
   url(r'^$',views.admin, name='admin'),
   url(r'^register/$', views.registerPage, name="register"),
   url(r'^login/$', views.loginPage, name="adminlogin"), 
   url(r'^logout/$',views.logoutUser,name="logout"),
   url(r'^contact/$',views.contact,name="contact"),
]
