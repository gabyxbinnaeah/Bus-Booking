from django.shortcuts import render
from .models import Driver, Bus, Book


# Create your views here.
def index(request):
    drivers = Driver.objects.all()
    return render(request, 'driver/index.html', {'drivers': drivers})

def dashboard(request):
    return render(request,'driver/dashboard.html')