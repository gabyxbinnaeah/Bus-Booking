from django.contrib import messages
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import render,redirect
from django.template import RequestContext
from driverapp.models import Bus
from userapp.models import Book

from .forms import BusForm, SeatsForm


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