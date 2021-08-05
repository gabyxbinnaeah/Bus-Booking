from .models import Bus
from django import forms


class BusForm(forms.ModelForm):
    class Meta:
        model=Bus
        fields=['source','dest','bus_name', 'date']