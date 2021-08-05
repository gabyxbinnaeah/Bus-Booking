from userapp.models import Book
from driverapp.models import Bus
from django import forms
from django.forms import fields


class UserCreationForm(forms.ModelForm):
    email = forms.EmailField()
    class Meta:
        model = Book
        fields = ['name','email','phone_number','fare','date','time','destination']
                  
class BusOwnerCreationForm(forms.ModelForm):
    
    class Meta:
        model = Bus
        fields = ['bus_name','destination','fare','date','time','fare']
        