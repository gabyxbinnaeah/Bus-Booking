from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Driver(models.Model):
    name = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    email = models.EmailField()
    Contact = models.CharField(max_length=10)
    

    def save_driver(self):
        self.save()

    def delete_driver(self):
        self.delete()
    
    @classmethod
    def update_driver(self):
        driver=Driver.objects.get_or_create()
        return driver
    
    def _str_(self):
        return self.email  


class Bus(models.Model):
    bus_name = models.CharField(max_length=30)
    source= models.CharField(max_length=30)
    destination = models.CharField(max_length=30)
    nos = models.IntegerField(default=0)
    rem = models.CharField(null=True, max_length=5,blank=True)
    fare = models.CharField(null=True, max_length=6)
    date = models.DateField()
    time = models.TimeField()
    name = models.CharField(max_length=30,null=True)
    password = models.CharField(max_length=30,null=True)
    email = models.EmailField(null=True)
    Contact = models.CharField(max_length=10,null=True)
    

    @classmethod
    def search_buses(cls, source, destination):
        return cls.objects.filter(source__icontains=source , destination__icontains=destination).all()
    def bus_details(cls):
        bus_details_list=cls.objects.all()
        return bus_details_list 

    def save_bus(self):
        self.save()

    def delete_bus(self):
        self.delete()
    
    @classmethod
    def update_bus(self):
        bus=Bus.objects.get_or_create()
        return bus


    def _str_(self):
        return self.bus_name



class Book(models.Model):
    BOOKED = 'B'
    CANCELLED = 'C'

    TICKET_STATUSES = ((BOOKED, 'Booked'),
                       (CANCELLED, 'Cancelled'),)
    email = models.EmailField()
    name = models.CharField(max_length=30)
    userid =models.ForeignKey(Driver,null=True,on_delete=models.CASCADE)
    busid=models.ForeignKey(Bus, null=True,on_delete=models.CASCADE, related_name='bus_id')
    source = models.CharField(max_length=30)
    destination = models.CharField(max_length=30,null=True ,blank=True)
    seat_no = models.CharField(max_length=30,null=True)
    fare = models.CharField(null=True, max_length=6)
    date = models.DateField()
    time = models.TimeField()
    status = models.CharField(choices=TICKET_STATUSES, default=BOOKED, max_length=2)
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    def _str_(self):
        return self.email
        
