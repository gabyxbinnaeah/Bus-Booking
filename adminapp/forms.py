from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Bus,Book,Admin
from userapp.models import Book
from driverapp.models import Bus
from django import forms
from django.forms import fields
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Admin

class DateInput(forms.DateInput):
    input_type = 'date'
class TimeInput(forms.TimeInput):
    input_type = 'time'


class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']


class CreatePasForm(forms.ModelForm):
    email = forms.EmailField()
    date = forms.DateField(widget=DateInput())
    time= forms.TimeField(widget=TimeInput())
    class Meta:
        model = Book
        fields = ['name','email','fare','date','time']
        widgets={'date' : DateInput(), 'time':TimeInput()}
                  
class BusOwnerCreationForm(forms.ModelForm):
    date = forms.DateField(widget=DateInput())
    time= forms.TimeField(widget=TimeInput())
    email = forms.EmailField()
    nos = forms.CharField(label='Number of seats')
    # class Meta:
    #     model = Driver
    #     fields = ['name','email','Contact']
            
    class Meta:
        model = Bus

        fields = ['name','email','Contact','bus_name','fare','date','time','source','destination','nos']
        widgets={'date' : DateInput(), 'time':TimeInput()}

class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']
