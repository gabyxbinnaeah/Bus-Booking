from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def seats(request):
    return render(request, 'seats.html')

def login(request):
    return render(request, 'auth/login.html')