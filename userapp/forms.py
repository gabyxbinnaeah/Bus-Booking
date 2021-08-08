from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms.models import ModelForm
from .models import *
from driverapp.models import Bus
from django import forms



class CreateUserForm(UserCreationForm):
    class Meta:
        model=User
        fields=['name','email','password1','password2']


class BookForm(forms.ModelForm):
    class Meta:
        model=Book
        fields=['busid','source','destination','date']



class BusForm(forms.ModelForm):
    class Meta:
        model=Bus
        fields=['source','destination','bus_name', 'date']
