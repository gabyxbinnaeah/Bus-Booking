from django.shortcuts import render,redirect
from userapp.models import Book
from driverapp.models import Bus
from .forms import UserCreationForm,BusOwnerCreationForm
from django.core.exceptions import ObjectDoesNotExist
from django.http.response import Http404
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


def create_pass(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('passengers-dash')
    context = {'form':form}
    return render(request,'admin_dash/create_form.html',context)

def update_pass(request,pk):
    order = Book.objects.get(id=pk)
    form = UserCreationForm(instance=order)
    if request.method == 'POST':
        form = UserCreationForm(request.POST,instance=order)
        if form.is_valid():
            form.save()
            return redirect('passengers-dash')
    context={'form':form}
    return render(request,'admin_dash/create_form.html',context)

def delete_pass(request, pk):
	order = Book.objects.get(id=pk)
	if request.method == "POST":
		order.delete()
		return redirect('passengers-dash')

	context = {'item':order}
	return render(request, 'admin_dash/delete.html', context)


def create_bus(request):
    form = BusOwnerCreationForm()
    if request.method == 'POST':
        form = BusOwnerCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('busses-dash')
    context = {'form':form}
    return render(request,'admin_dash/create_bus_form.html',context)

def update_bus(request,pk):
    order = Bus.objects.get(id=pk)
    form = BusOwnerCreationForm(instance=order)
    if request.method == 'POST':
        form = BusOwnerCreationForm(request.POST,instance=order)
        if form.is_valid():
            form.save()
            return redirect('busses-dash')
    context={'form':form}
    return render(request,'admin_dash/create_bus_form.html',context)

def delete_bus(request, pk):
	order = Bus.objects.get(id=pk)
	if request.method == "POST":
		order.delete()
		return redirect('busses-dash')

	context = {'item':order}
	return render(request, 'admin_dash/delete_bus.html', context)

def passenger(request,pk_test):
    try:
        passenger = Book.objects.get(id=pk_test)
    except ObjectDoesNotExist:
        raise Http404()
    
    context={'passenger':passenger}
    return render(request,'admin_dash/individual_pass.html', context)

def driver(request,pk_test):
    try:
        driver = Bus.objects.get(id=pk_test)
    except ObjectDoesNotExist:
        raise Http404()
    
    context={'bus':driver}
    return render(request,'admin_dash/individual_driver.html',context)