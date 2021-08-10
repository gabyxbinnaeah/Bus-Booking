from datetime import date
from django.http.response import HttpResponse, HttpResponseRedirect, Http404
from decimal import Decimal
from .forms import *
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from django.template import RequestContext
from django.urls import reverse
from driverapp.models import Bus
from userapp.models import Book
from .models import Book
from .forms import BusForm, SeatsForm,CreateUserForm,BookForm


today = date.today()


@login_required(login_url='loginpage')
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
@login_required(login_url='loginpage')
def booking(request):
    form = SeatsForm()
    if request.method == 'POST':
        form = SeatsForm(request.POST)
        if form.is_valid():
            seat = form.cleaned_data.get('seat_no')
            form.save()
            return redirect('confirm_booking')
    else:
        form = SeatsForm()
    return render(request, 'main/booking.html', {'form': form})
@login_required(login_url='loginpage')
def confirm_booking(request):

    seats=Book.objects.all().latest('created_at')
    seat=seats.__dict__
    # seat_no=seat.count()
    return render(request, 'main/confirm_book.html', {'seats': seats,'seat': seat})


def mytravels(request):
    mytravel=Book.objects.last()
    return render(request,'main/mytravel.html',{'mytravel':mytravel})


# Create your views here.
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
    return render(request,'main/checkout.html',{'books':books})

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

