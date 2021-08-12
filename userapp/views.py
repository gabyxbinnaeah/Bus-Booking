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


from django.http import HttpResponse, JsonResponse
import requests
from requests.auth import HTTPBasicAuth
import json
from . mpesa_credentials import MpesaAccessToken, LipanaMpesaPpassword
from django.views.decorators.csrf import csrf_exempt
from .models import MpesaPayment
from .models import Fare as Transfee
from .forms import FareForm

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
    current_user=request.user.email
    mytravel=Book.show_bookings(current_user)
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
    books=Book.objects.last()
    return render(request,'main/checkout.html',{'books':books})

def update(request,pk):
    book = Book.objects.get(id=pk)
    form=SeatsForm(instance=book)
    if request.method == 'POST':
        form = SeatsForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('mytravels')
        
        
    return render(request, 'update.html', {'form':form})


def delete_booking(request, pk):
	book = Book.objects.get(id=pk)
	if request.method == "POST":
		book.delete()
		return redirect('mytravels')

	context = {'book':book}
	return render(request, 'delete.html', context)

# Mpesa payment
def seats(request):
    return render(request,'seats.html')



def lipa_fare(request):
    # redirect = request.GET.get('index') 
    return render(request,'fare.html')

def getAccessToken(request):
    consumer_key = 'yEXHHx5zjKuTWUqVexTUoCd8NNWj8bgu'
    consumer_secret = 'YlY4JGJbL4Ro5F6e'
    api_URL = 'https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials'

    r = requests.get(api_URL, auth=HTTPBasicAuth(consumer_key, consumer_secret))
    mpesa_access_token = json.loads(r.text)
    validated_mpesa_access_token = mpesa_access_token['access_token']

    return HttpResponse(validated_mpesa_access_token)


def lipa_na_mpesa_online(request):
    if request.method=="POST" and 'hidden_details' in request.POST:
        transaction_number=request.POST.get('phone_number')
        cell= str(254)+str(int(transaction_number))
        remiting_number=int(cell)

        fare_charges=request.POST.get('fare')
        
        


        access_token = MpesaAccessToken.validated_mpesa_access_token
        api_url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"
        headers = {"Authorization": "Bearer %s" % access_token}
        request = {

            "BusinessShortCode": LipanaMpesaPpassword.Business_short_code,
            "Password": LipanaMpesaPpassword.decode_password,
            "Timestamp": LipanaMpesaPpassword.lipa_time,
            "TransactionType": "CustomerPayBillOnline",
            "Amount":int(fare_charges),
            "PartyA": remiting_number,  # replace with your phone number to get stk push
            "PartyB": LipanaMpesaPpassword.Business_short_code,
            "PhoneNumber": remiting_number,  # replace with your phone number to get stk push
            "CallBackURL": "https://sandbox.safaricom.co.ke/mpesa/",
            "AccountReference": "Eazy Bus Company",
            "TransactionDesc": "Testing stk push"
        }

        response = requests.post(api_url, json=request, headers=headers)
        return HttpResponse(f'Kindly check your phone {remiting_number} and enter mpesa pin to succesfully pay fare')


@csrf_exempt
def register_urls(request):
    access_token = MpesaAccessToken.validated_mpesa_access_token
    api_url = "https://sandbox.safaricom.co.ke/mpesa/c2b/v1/registerurl"
    headers = {"Authorization": "Bearer %s" % access_token}
    options = {"ShortCode": LipanaMpesaPpassword.Test_c2b_shortcode,

               "ResponseType": "Completed",
               "ConfirmationURL": "http://127.0.0.1:8000/api/v1/c2b/confirmation",
               "ValidationURL": "http://127.0.0.1:8000/api/v1/c2b/validation"}
    response = requests.post(api_url, json=options, headers=headers)

    return HttpResponse(response.text)


@csrf_exempt
def call_back(request):
    pass


@csrf_exempt
def validation(request):

    context = {
        "ResultCode": 0,
        "ResultDesc": "Accepted"
    }
    return JsonResponse(dict(context))


@csrf_exempt
def confirmation(request):
    mpesa_body =request.body.decode('utf-8')
    mpesa_payment = json.loads(mpesa_body)

    payment = MpesaPayment(
        first_name=mpesa_payment['FirstName'],
        last_name=mpesa_payment['LastName'],
        middle_name=mpesa_payment['MiddleName'],
        description=mpesa_payment['TransID'],
        phone_number=mpesa_payment['MSISDN'],
        amount=mpesa_payment['TransAmount'],
        reference=mpesa_payment['BillRefNumber'],
        organization_balance=mpesa_payment['OrgAccountBalance'],
        type=mpesa_payment['TransactionType'],

    )
    payment.save()

    context = {
        "ResultCode": 0,
        "ResultDesc": "Accepted"
    }

    return JsonResponse(dict(context))


def Fare(request):
    if request.method == 'POST' and "fare_details" in request.POST:
            cell_number=request.POST.get('phone_number')
            fare=request.POST.get('fare')
            new_details=Transfee(phone_number = cell_number, fare = fare)
            new_details.save()
            context={
                "new_details":new_details,

            }
            return render( request,'fare.html' ,context) 
    else:
        form = FareForm() 
    return render(request, 'newbook.html', {'form': form}) 


def about_us(request):
    return render(request,'about_us.html')

def succes(request):
	return render(request, "success.html")

def contact_us(request):
	return render(request, "contact_us.html")