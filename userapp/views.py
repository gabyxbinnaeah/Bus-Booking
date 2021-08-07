from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .models import *
# Create your views here.

def index(request):

    return render(request, 'index.html')

@csrf_exempt
def seats(request):
    seat=request.GET.get('count')
    total=request.GET.get('total')
    # total_seats=Bus.objects.get(nos=seat)
    # total_fare=Bus.objects.get(fare=total)

    print(seat,total)


    return render(request, 'seats.html')

def test(request):
    return render(request, 'test.html')
def login(request):
    return render(request, 'auth/login.html')