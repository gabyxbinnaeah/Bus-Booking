from .models import Book
from driverapp.models import Bus
from django import forms
from django.forms import fields
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Driver

class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']


class CreatePasForm(forms.ModelForm):
    email = forms.EmailField()
    class Meta:
        model = Driver
        fields = ['name','email','Contact']
                   
class DateInput(forms.DateInput):
    input_type = 'date'
class TimeInput(forms.TimeInput):
    input_type = 'time'
            
class BusOwnerCreationForm(forms.ModelForm):
    date = forms.DateField(widget=DateInput())
    time= forms.TimeField(widget=TimeInput())
    nos = forms.CharField(label='Number of seats')
    source =forms.CharField(label = "From")
    destination =forms.CharField(label = "To")
    class Meta:
        model = Bus
        fields = ['name','email','Contact','bus_name','fare','date','time','source','destination','nos']
        widgets={'date' : DateInput(), 'time':TimeInput()}