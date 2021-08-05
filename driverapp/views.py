from django.shortcuts import redirect, render
from .models import Driver, Bus, Book
from django.contrib.auth.decorators import login_required
# from .forms import CreateUserForm
from .forms import CreateUserForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout

# Create your views here.
# @login_required
def dashboard(request):
    drivers = Driver.objects.all()
    bus = Bus.objects.all()
    # if not request.user.is_authenticated:
    #     return render(request, 'registration/login.html')
    # else:
    return render(request, 'driver/dashboard.html',{"drivers":drivers, "bus":bus})

@login_required
def delete_bus(request):
    bu_id = request.POST['id']
    bus = Bus.objects.get(id = bu_id)
    bus.delete()
    return render(request, 'driver/dashboard.html',{"bus":bus} )
    # return HttpResponseRedirect('/driverapp/manage_busees/')

def customer(request):
    customer = Bus.objects.all()
    return render(request, 'customer.html',{'customer':customer})
     

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

            return redirect('dashboard')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password =request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('loginpage')
            else:
                messages.info(request, 'Username or password is incorrect')

      
    return render(request,'registration/login.html')

# def dashboard(request):
#     return render(request, 'driver/dashboard.html')


def add_bus(request):
    bus = Bus.objects.all()
    return render(request, 'driver/bus_added.html')
