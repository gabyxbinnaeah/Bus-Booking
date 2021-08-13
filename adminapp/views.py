from django.shortcuts import render,redirect
from userapp.models import Book
from driverapp.models import Bus
from .forms import CreatePasForm,BusOwnerCreationForm
from django.core.exceptions import ObjectDoesNotExist
from django.http.response import Http404
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm 
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Admin 
from django.shortcuts import get_object_or_404
from .filter import OrderFilter,OrderFilterPassenger

# Create your views here.

def registerPage(request):
	if request.user.is_authenticated:
		return redirect('passengers-dash')
	else:
		form = CreateUserForm()
		if request.method == 'POST':
			form = CreateUserForm(request.POST)
			if form.is_valid():
				form.save()
				user = form.cleaned_data.get('username')
				messages.success(request, 'Account was created for ' + user)

				return redirect('superapplogin')
			

		context = {'form':form}
		return render(request, 'accounts/register.html', context)



def loginPage(request):
	if request.user.is_authenticated:
		return redirect('passengers-dash')
	else:
		if request.method == 'POST':
			username = request.POST.get('username')
			password =request.POST.get('password')

			user = authenticate(request, username=username, password=password)

			if user is not None:
				login(request, user)
				return redirect('passengers-dash')
			else:
				messages.info(request, 'Username OR password is incorrect')

		context = {}
		return render(request, 'accounts/login.html', context)

def logoutUser(request):
	logout(request)
	return redirect('superapplogin')

# @login_required(login_url='superapplogin') 
# def admin(request):
#     return render(request, 'adminapp/index.html') 

@login_required(login_url='superapplogin') 
def contact(request):
	return render(request, 'adminapp/contact.html')

@login_required(login_url='superapplogin')
def index(request):

    bus = Bus.objects.all()
    book= Book.objects.all()
    total_customers = book.count()
    total_busses = bus.count()
    myFilter = OrderFilterPassenger(request.GET,queryset=book)
    book = myFilter.qs
    return render(request, 'admin_dash/passengers.html',{'book':book[::-1],"bus":bus[::-1],'total_busses':total_busses,'total_customers':total_customers,'myFilter':myFilter})

@login_required(login_url='superapplogin')
def busses(request):
    bus = Bus.objects.all()
    book= Book.objects.all()
    total_customers = book.count()
    total_busses = bus.count()
    myFilter = OrderFilter(request.GET,queryset=bus)
    bus = myFilter.qs
    return render(request, 'admin_dash/busses.html',{'book':book[::-1],"bus":bus[::-1],'total_busses':total_busses,'total_customers':total_customers,'myFilter':myFilter})


def create_pass(request):
    form = CreatePasForm()
    if request.method == 'POST':
        form = CreatePasForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('passengers-dash')
    context = {'form':form}
    return render(request,'admin_dash/create_form.html',context)

def update_pass(request,pk):
    order = Book.objects.get(id=pk)
    form = CreatePasForm(instance=order)
    if request.method == 'POST':
        form = CreatePasForm(request.POST,instance=order)
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
            return redirect('buses-dash')
    context = {'form':form}
    return render(request,'admin_dash/create_bus_form.html',context)

def update_bus(request,pk):
    order = Bus.objects.get(id=pk)
    form = BusOwnerCreationForm(instance=order)
    if request.method == 'POST':
        form = UserCreationForm(request.POST,instance=order)
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

def driver_details(request):
    bus = Bus.objects.all()
    return render(request,'admin_dash/driver.html',{"buss":bus[::-1]})

def driver_route(request):
    route = Bus.objects.all()
    return render(request,'admin_dash/route.html',{'route':route})
def search_request(request):
    if 'query' in request.POST and request.GET['query']: 
        search = request.GET.get('query')
        search_buses= Bus.search_buses(search)
        message= f'{search}'
        context = {"message":messages,"businesses":search_buses}
        
        return render(request,'admin_dash/search.html',context)

    else:
        message="You haven't searched for any item"
        return render(request,'admin_dash/search.html',{"message":message})   
     
def search_passengers(request):
    if 'query' in request.GET and request.GET['query']:
        search_term = request.GET.get("query")
        searched_term = Bus.search_by_title(search_term)
        message = f'{search_term}'
        
        return render(request, 'admin_dash/search.html',{'message':message,"articles":search_term})
    
    else:
        message = "You haven't searched for any term"
        return render(request,'admin_dash/search.html',{"message":message})   
     