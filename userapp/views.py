from django.http.response import HttpResponse, HttpResponseRedirect, Http404
from userapp.models import Book
from decimal import Decimal
from django.shortcuts import render,redirect
from .forms import *
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import BusForm
from django.http import HttpResponseRedirect
from driverapp.models import Bus

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


def search_bus(request):
    if request.method=='POST':
        source=request.POST.get('source')
        dest=request.POST.get('dest')
        date=request.POST.get('date')
        bus_list=Bus.objects.filter(source=source,dest=dest,date=date)
        print(bus_list)
        context={}
        if bus_list:
            return render(request,'list.html',locals())
        else:
            context["error"]="no buses availble for that destination"
            return render(request,'search_bus.html',context)
    else:

        return render(request,'search_bus.html')
    

def booking(request):
    if request.method=='POST':
        busid=request.POST.get('busid')
        seats=int(request.POSt.get('nos'))
        bus=Bus.objects.get(id=busid)
        context={}
        if bus:
            if bus.rem > int(seats):
                name=bus.bus_name
                cost=int(seats)*bus.price
                source=bus.source
                dest=bus.dest
                nos=Decimal(bus.nos)
                price=bus.price
                date=bus.date
                time=bus.time
                userid=request.user.id
                rem=bus.rem -seats
                Bus.objects.filter(id=busid).update(rem=rem)
                book=Book.objects.create(time=time,date=date,price=price,nos=nos,dest=dest,source=source,bus_name=name,status='BOOKED')
                print('book id ',book.id)
               
                return render(request,'booking.html',locals())
            else:
                context["error"]="select few seats"
                return render(request,'search_bus.html',context)
        else:
     
            return render(request,'search_bus.html')



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
