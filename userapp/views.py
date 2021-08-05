from django.shortcuts import render
from .forms import BusForm
from django.http import HttpResponseRedirect

def index(request):
    if request.method == 'POST':
        form=BusForm(request.POST,request.FILES)
        if form.is_valid():
            bus=form.save(commit=False)
            bus.save()
    
            return HttpResponseRedirect(request.path_info)
    else:
        form = BusForm()
    return render(request, 'main/index.html',{'form':form}) 
