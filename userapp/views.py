from datetime import date
from decimal import Decimal

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.template import RequestContext
from django.urls import reverse
from driverapp.models import Bus

from userapp.models import Book


today = date.today()

from .forms import BusForm, SeatsForm,CreateUserForm,BookForm


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

def booking(request,id):
    form = SeatsForm()
    if request.method == 'POST':
        form = SeatsForm(request.POST)
        if form.is_valid():
            seat = form.cleaned_data.get('seat_no')
            form.save()
            return HttpResponseRedirect(self.request.path_info)
    else:
        form = SeatsForm()
    seats=Book.objects.all().latest('created_at')
    seat=seats.__dict__
    context={
        'form': form,
        'seats': seats,
        'seat': seat
    }
    return render(request, 'main/booking.html', context)


def registeruser(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account Created Successfully!. Check out our Email later :)')

            return redirect('loginpage')
    else:
        form = CreateUserForm
    context = {
            
            'form':form,
                        }

    return render(request,'registration/register.html',context)

def loginpage(request):
    if request.user.is_authenticated:

            return redirect('index')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password =request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('index')
            else:
                messages.info(request, 'Username or password is incorrect')

      
    return render(request,'registration/login.html')


def logout_page(request):
    logout(request) 
    return redirect('loginpage')

def checkout(request):
    books=Book.objects.all()
    return render(request,'checkout.html',{'books':books})

def update(request,pk):
    book = Book.objects.get(pk=pk)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            url = reverse('index', kwargs={'pk': pk})
            return render(request, 'index.html', {'url': url})
        else:
            form = BookForm(instance=book)
    else:
        form = BookForm(instance=book)
    return render(request, 'update.html', {'form':form, 'book':book})

def delete_booking(request, pk):
    book = Book.objects.get(pk=pk)
    book.delete()
    return render(request, 'index.html')

def contact_us(request):
    return render(request, 'contact_us.html')

def aboutus(request):
    return render(request, 'about_us.html')