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

class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']


class CreatePasForm(forms.ModelForm):
    email = forms.EmailField()
    class Meta:
        model = Book
        fields = ['name','email','fare','date','time']
                  
class BusOwnerCreationForm(forms.ModelForm):
    
    class Meta:
        model = Bus
        fields = ['bus_name','fare','date','time']
        

class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']
