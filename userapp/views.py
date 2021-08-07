from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .models import Bus
# Create your views here.

def index(request):

    return render(request, 'index.html')

@csrf_exempt
def seats(request):
    seat=request.GET.get('count')
    total=request.GET.get('total')
    # no_of_seat=Bus.objects.filter()
    print(seat, total)


    return render(request, 'seats.html')
    
def login(request):
    return render(request, 'auth/login.html')