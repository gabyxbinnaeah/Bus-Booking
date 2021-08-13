from django.shortcuts import render,redirect
from .models import Book
from driverapp.models import Bus
from .forms import CreatePasForm,BusOwnerCreationForm
from django.core.exceptions import ObjectDoesNotExist
from django.http.response import Http404
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm 
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Driver
from django.shortcuts import get_object_or_404
from adminapp.filter import OrderFilter
# Create your views here.

def registerDriver(request):
	if request.user.is_authenticated:
		return redirect('driver')
	else:
		form = CreateUserForm()
		if request.method == 'POST':
			form = CreateUserForm(request.POST)
			if form.is_valid():
				form.save()
				user = form.cleaned_data.get('username')
				messages.success(request, 'Account was created for ' + user)

				return redirect('driverlogin')
			

		context = {'form':form}
		return render(request, 'registration/register.html', context)



def loginPage(request):
	if request.user.is_authenticated:
		return redirect('drivers_dash')
	else:
		if request.method == 'POST':
			username = request.POST.get('username')
			password =request.POST.get('password')

			user = authenticate(request, username=username, password=password)

			if user is not None:
				login(request, user)
				return redirect('busses-dash')



			else:
				messages.info(request, 'Username OR password is incorrect')

		context = {}
		return render(request, 'registration/login.html', context)

def logoutDriver(request):
	logout(request)
	return redirect('driverlogin')

# @login_required(login_url='driverlogin') 
# def admin(request):
#     return render(request, 'driver/home.html') 

@login_required(login_url='driverlogin')
def home(request):

    bus = Bus.objects.all()
    book= Book.objects.all()
    total_drivers = book.count()
    total_busses = bus.count()
    return render(request, 'driver_dash/driver.html',{'book':book[::-1],"bus":bus[::-1],'total_busses':total_busses,'total_drivers':total_drivers})

@login_required(login_url='driverlogin')
def busses(request):
    bus = Bus.objects.all()
    book= Book.objects.all()
    total_drivers = book.count()
    total_busses = bus.count()
    myFilter = OrderFilter(request.GET,queryset=bus)
    bus = myFilter.qs
    return render(request, 'driver_dash/busses.html',{'book':book[::-1],"bus":bus[::-1],'total_busses':total_busses,'total_drivers':total_drivers, "myFilter":myFilter})


def create_driver(request):
    form = CreatePasForm()
    if request.method == 'POST':
        form = CreatePasForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('drivers_dash')
    context = {'form':form}
    return render(request,'driver_dash/create_form.html',context)

def update_driver(request,pk):
    order = Book.objects.get(id=pk)
    form = CreatePasForm(instance=order)
    if request.method == 'POST':
        form = CreatePasForm(request.POST,instance=order)
        if form.is_valid():
            form.save()
            return redirect('drivers_dash')
    context={'form':form}
    return render(request,'driver_dash/create_form.html',context)

def delete_driver(request, pk):
	order = Book.objects.get(id=pk)
	if request.method == "POST":
		order.delete()
		return redirect('drivers_dash')

	context = {'item':order}
	return render(request, 'driver_dash/delete.html', context)


def add_bus(request):
    form = BusOwnerCreationForm()
    if request.method == 'POST':
        form = BusOwnerCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('busses-dash')
    context = {'form':form}
    return render(request,'driver_dash/create_bus_form.html',context)

def update_bus(request,pk):
    bus = Bus.objects.get(id=pk)
    form = BusOwnerCreationForm(instance=bus)
    if request.method == 'POST':
        form = UserCreationForm(request.POST,instance=bus)
        if form.is_valid():
            form.save()
            return redirect('busses-dash')
    context={'form':form}
    return render(request,'driver_dash/create_bus_form.html',context)

def delete_bus(request, pk):
	order = Bus.objects.get(id=pk)
	if request.method == "POST":
		order.delete()
		return redirect('busses-dash')

	context = {'item':order}
	return render(request, 'driver_dash/delete_bus.html', context)

def driver(request,pk_test):
    try:
        driver = Driver.objects.get(id=pk_test)
    except ObjectDoesNotExist:
        raise Http404()
    
    context={'driver':driver}
    return render(request,'driver_dash/individual_driver.html',context)


def driver_route(request):
    route = Bus.objects.all()
    return render(request,'driver_dash/route.html',{'route':route})


def driver_details(request):
    bus = Bus.objects.all()
    return render(request,'driver_dash/driver.html',{"buss":bus[::-1]})

def search_request(request):
    if 'query' in request.POST and request.GET['query']: 
        search = request.GET.get('query')
        search_business= Business.search_by_title(search)
        messages= f'{search}'
        context = {"message":messages,"businesses":search_businesses}
        
        return render(request,'driver_dash/search.html',context)

    else:
        message="You haven't searched for any item"
        return render(request,'driver_dash/search.html',{"message":message})   
        
