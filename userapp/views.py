from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from .forms import BusForm
from django.http import HttpResponseRedirect
from driverapp.models import Bus


def index(request):
    buses = Bus.objects.all()
    return render(request, 'index.html')

def seats(request):
    return render(request, 'seats.html')

def login(request):
    return render(request, 'auth/login.html')
    if request.method == 'POST':
        form=BusForm(request.POST,request.FILES)
        if form.is_valid():
            source=form.cleaned_data['source']
            dest=form.cleaned_data['dest']
            search_bus=Bus.search_buses(source,dest)
            return render(request, 'main/index.html',{'form':form,"buses":search_bus}) 
    else:
        form = BusForm()
    return render(request, 'main/index.html',{'form':form}) 
