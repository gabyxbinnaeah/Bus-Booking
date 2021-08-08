from django import forms
from .models import Book

class BookBus(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('seat_no',)