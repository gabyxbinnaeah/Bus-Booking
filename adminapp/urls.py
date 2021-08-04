from django.urls import path
from . import views

urlpatterns=[
    path('',views.index, name='passengers-dash'),
    path('busses/',views.busses, name='busses-dash'),
]