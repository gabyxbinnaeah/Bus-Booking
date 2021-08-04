from . import views
from django.urls import path

urlpatterns=[
    path('userapp/',views.index, name='user'),
]