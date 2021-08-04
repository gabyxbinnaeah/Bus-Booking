from .models import Bus
from django import forms


class BusForm(forms.ModelForm):
    class Meta:
        model=Bus
        fields=['dest', 'date', 'bus_name','source']