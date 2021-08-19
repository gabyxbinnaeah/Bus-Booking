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
from userapp.decorators import unauthenticated,allowed_users
from django.contrib.auth.models import Group

# Create your views here.

# def registerDriver(request):
# 	if request.user.is_authenticated:
# 		return redirect('driver')
# 	else:
# 		form = CreateUserForm()
# 		if request.method == 'POST':
# 			form = CreateUserForm(request.POST)
# 			if form.is_valid():
# 				form.save()
# 				user = form.cleaned_data.get('username')
# 				messages.success(request, 'Account was created for ' + user)

# 				return redirect('driverlogin')
			

# 		context = {'form':form}
# 		return render(request, 'register_driver/register.html', context)

def registerDriver(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            driver=form.save()
            group=Group.objects.get(name='driver')
            driver.groups.add(group)
            messages.success(request, 'Account Created Successfully!. Check out our Email later :)')

            return redirect('driverlogin')
    else:
        form = CreateUserForm
    context = {'form':form}

    return render(request, 'register_driver/register.html', context)



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
		return render(request, 'register_driver/login.html', context)

def logoutDriver(request):
	logout(request)
	return redirect('driverlogin')

# @login_required(login_url='driverlogin') 
# def admin(request):
#     return render(request, 'driver/home.html') 

@allowed_users(allowed_roles=['driver','admin'])
def home(request):

    bus = Bus.objects.all()
    book= Book.objects.all()
    total_drivers = book.count()
    total_busses = bus.count()
    return render(request, 'driver_dash/driver.html',{'book':book[::-1],"bus":bus[::-1],'total_busses':total_busses,'total_drivers':total_drivers})

@allowed_users(allowed_roles=['driver','admin'])
def busses(request):
    bus = Bus.objects.all()
    book= Book.objects.all()
    total_drivers = book.count()
    total_busses = bus.count()
    return render(request, 'driver_dash/busses.html',{'book':book[::-1],"bus":bus[::-1],'total_busses':total_busses,'total_drivers':total_drivers})

@allowed_users(allowed_roles=['driver','admin'])
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
            return redirect('busses-dash')
    context={'form':form}
    return render(request,'driver_dash/create_form.html',context)

@allowed_users(allowed_roles=['driver','admin'])
def delete_driver(request, pk):
	order = Book.objects.get(id=pk)
	if request.method == "POST":
		order.delete()
		return redirect('drivers_dash')

	context = {'item':order}
	return render(request, 'driver_dash/delete.html', context)

@allowed_users(allowed_roles=['driver','admin'])
def add_bus(request):
    form = BusOwnerCreationForm()
    if request.method == 'POST':
        form = BusOwnerCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('busses-dash')
    context = {'form':form}
    return render(request,'driver_dash/create_bus_form.html',context)
@allowed_users(allowed_roles=['driver','admin'])
def update_bus(request,pk):
    bus = Bus.objects.get(id=pk)
    form = BusOwnerCreationForm(instance=bus)
    if request.method == 'POST':
        form = BusOwnerCreationForm(request.POST,instance=bus)
        if form.is_valid():
            form.save()
            return redirect('busses-dash')
    context={'form':form}
    return render(request,'driver_dash/create_bus_form.html',context)


@allowed_users(allowed_roles=['driver','admin'])
def delete_bus(request, pk):
	order = Bus.objects.get(id=pk)
	if request.method == "POST":
		order.delete()
		return redirect('busses-dash')

	context = {'item':order}
	return render(request, 'driver_dash/delete_bus.html', context)
@allowed_users(allowed_roles=['driver','admin'])
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