from userapp.forms import BookBus
from django.shortcuts import redirect, render
from django.views.decorators.csrf import csrf_exempt
from .models import *
from django.contrib.auth.models import User
from django.contrib import messages
from driverapp.models import Bus
from userapp.models import Book

from .forms import BusForm, SeatsForm



# Create your views here.

def index(request):

    return render(request, 'index.html')

@csrf_exempt
def seats(request):
    seat=request.GET.get('count')
    total=request.GET.get('total')
    # total_seats=Bus.objects.get(nos=seat)
    # total_fare=Bus.objects.get(fare=total)

    print(seat,total)


    return render(request, 'seats.html')

def test(request):
    if request.method == 'POST':
        form = BookBus(request.POST,request.FILES)
        print(form.errors)
        if form.is_valid():
            post = form.save(commit=False)
         
            post.save()
            return redirect('test')
    else:
        form = BookBus()
    return render(request,'test.html', {"form":form})


def login(request):
    return render(request, 'auth/login.html')


def index(request):
    buses = Bus.objects.all()
    if request.method == 'POST':
        form=BusForm(request.POST,request.FILES)
        if form.is_valid():
            source=form.cleaned_data['source']
            destination=form.cleaned_data['destination']
            search_bus=Bus.search_buses(source,destination)
            if search_bus:
                messages.success(request, 'Found some buses for you')
            else:
                messages.error(request, 'Oops! No buses found from your search.')
            return render(request, 'main/index.html',{'form':form,"buses":search_bus}) 
        else:
            messages.warning(request,"No available buses.")
    else:
        form = BusForm()
    return render(request, 'main/index.html',{'form':form}) 

def booking(request):
    form = SeatsForm()
    if request.method == 'POST':
        form = SeatsForm(request.POST,request.FILES)
        if form.is_valid():
            form.save(commit=False)
            form.save()
            return redirect('confirm_booking')
    else:
        form = SeatsForm()
    return render(request, 'main/booking.html', {'form': form})

def confirm_booking(request):
    form = SeatsForm()
    seat=Book.objects.all()
    return render(request, 'main/confirm_book.html', {'form': form,'seat': seat})
