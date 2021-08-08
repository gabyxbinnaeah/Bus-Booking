from driverapp.models import Bus
from .models import Book
from django import forms

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
        fields=['seat_no']
    
