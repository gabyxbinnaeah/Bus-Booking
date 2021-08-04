from django.shortcuts import render
from userapp.models import Book
from driverapp.models import Bus

# Create your views here.
def index(request):
    bus = Bus.objects.all()
    book= Book.objects.all()
    total_customers = book.count()
    total_busses = bus.count()
    return render(request, 'admin_dash/passengers.html',{'book':book[::-1],"bus":bus[::-1],'total_busses':total_busses,'total_customers':total_customers})

def busses(request):
    bus = Bus.objects.all()
    book= Book.objects.all()
    total_customers = book.count()
    total_busses = bus.count()
    return render(request, 'admin_dash/busses.html',{'book':book[::-1],"bus":bus[::-1],'total_busses':total_busses,'total_customers':total_customers})


