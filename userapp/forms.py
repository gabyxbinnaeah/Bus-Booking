from driverapp.models import Bus
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms.models import ModelForm
from .models import *


class DateInput(forms.DateInput):
    input_type = 'date'

class BusForm(forms.ModelForm):
    class Meta:
        model=Bus
        fields=['source','destination','bus_name', 'date']
        widgets={
            'date':DateInput()
        }
        
class SeatsForm(forms.ModelForm):
    
    class Meta:
        model = Book
        fields=['seat_no','name','email','date','fare']


class CreateUserForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username','email','password1','password2']


class BookForm(forms.ModelForm):
    class Meta:
        model=Book
        fields=['busid','source','destination','date']


class BusForm(forms.ModelForm):
    class Meta:
        model=Bus
        fields=['source','destination','bus_name', 'date']
