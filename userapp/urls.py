from . import views
from django.urls import path

urlpatterns=[
    path('user/',views.index, name='index'),
]