from django.shortcuts import render
from .models import Driver, Bus, Book
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    drivers = Driver.objects.all()
    bus = Bus.objects.all()
    if not request.user.is_authenticated:
        return render(request, 'registration/login.html')
    else:
        return render(request, 'driver/index.html',{"drivers":drivers, "bus":bus})

def login(request):
    return render(request, 'registration/login.html')

def manage_bus(request):
    name = request.bus
    driver = Driver.objects.get(name = name)
    bus = Bus.objects.get(driverapp = driver)
  
    bus = Bus.objects.filter(driver = driver)

    return render(request, 'driver/index.html', {'bus':bus})


def delete(request):
    bu_id = request.POST['id']
    bus = Bus.objects.get(id = bu_id)
    bus.delete()
    return render(request, 'driver/index.html' )
    # return HttpResponseRedirect('/driverapp/manage_busees/')
    
# def bus(request):
#     bus = Bus.objects.all()
#     return render(request, 'driver/index.html',{"bus":bus})

# def registration(request):
#     if request.method == 'POST':
#         form = RegisterForm(request.POST)
#         if form.is_valid():
#             username = form.cleaned_data.get('username')
#             form.save()
#             return redirect('login')
#     else:
#         form = RegisterForm()
#     context = {
#         'form':form,
#     }
#     return render(request, 'registration/register.html', context)