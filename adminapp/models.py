from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Admin(models.Model):
    name = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    email = models.EmailField()

    def save_admin(self):
        self.save()

    def delete_admin(self):
        self.delete()
    
    @classmethod
    def update_admin(self):
        admin=Admin.objects.get_or_create()
        return admin
    
    def __str__(self):
        return self.email  


class Bus(models.Model):
    bus_name = models.CharField(max_length=30)
    source = models.CharField(max_length=30)
    dest = models.CharField(max_length=30)
    nos = models.IntegerField(default=0)
    rem = models.CharField(null=True, max_length=5)
    fare = models.CharField(null=True, max_length=6)
    date = models.DateField()
    time = models.TimeField()
    

    def save_bus(self):
        self.save()

    def delete_bus(self):
        self.delete()
    
    @classmethod
    def update_bus(self):
        bus=Bus.objects.get_or_create()
        return bus

    @classmethod
    def bus_details(cls):
        bus_details_list=cls.objects.all()
        return bus_details_list 

    def __str__(self):
        return self.bus_name



class Book(models.Model):
    BOOKED = 'B'
    CANCELLED = 'C'

    TICKET_STATUSES = ((BOOKED, 'Booked'),
                       (CANCELLED, 'Cancelled'),)
    email = models.EmailField()
    name = models.CharField(max_length=30)
    userid =models.ForeignKey(Admin,null=True,on_delete=models.CASCADE)
    busid=models.ForeignKey(Bus, null=True,on_delete=models.CASCADE)
    source = models.CharField(max_length=30)
    dest = models.CharField(max_length=30,null=True ,blank=True)
    seat_no = models.CharField(max_length=30,null=True)
    fare = models.CharField(null=True, max_length=6)
    date = models.DateField()
    time = models.TimeField()
    status = models.CharField(choices=TICKET_STATUSES, default=BOOKED, max_length=2)

    def __str__(self):
        return self.email

    def save_booking(self):
        self.save()

    def delete_booking(self):
        self.delete()

    @classmethod
    def update_booking(self):
        book=Book.objects.get_or_create()
        return book

