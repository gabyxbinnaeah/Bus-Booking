from django.db import models
from adminapp.models import Admin,User


# Create your models here.
class Bus(models.Model):
    bus_name = models.CharField(max_length=30)
    source = models.CharField(max_length=30)
    destination = models.CharField(max_length=30)
    number_of_Seats = models.IntegerField(default=0)
    rem = models.CharField(null=True, max_length=5)
    fare = models.CharField(null=True, max_length=6)
    date = models.DateField()
    time = models.TimeField()
    admin = models.ForeignKey(Admin,on_delete=models.CASCADE,blank=True,null=True,related_name='admin')
    

    def __str__(self):
        return self.bus_name
