from driverapp.models import Bus
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