from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms.models import ModelForm
from .models import *
from .models import Bus
from django import forms



class CreateUserForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username','email','password1','password2']


class BookForm(forms.ModelForm):
    class Meta:
        model=Book
        fields=['busid','source','dest','date']



class BusForm(forms.ModelForm):
    class Meta:
        model=Bus
        fields=['source','dest','bus_name', 'date']