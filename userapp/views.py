from userapp.forms import BookBus
from django.shortcuts import redirect, render
from django.views.decorators.csrf import csrf_exempt
from .models import *
from django.contrib.auth.models import User

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
    if request.method == 'POST':
        form = BookBus(request.POST,request.FILES)
        print(form.errors)
        if form.is_valid():
            post = form.save(commit=False)
         
            post.save()
            return redirect('test')
    else:
        form = BookBus()
    return render(request,'test.html', {"form":form})


def login(request):
    return render(request, 'auth/login.html')