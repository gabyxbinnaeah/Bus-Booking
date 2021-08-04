from django.db import models
from adminapp.models import Admin


# Create your models here.
class Bus(models.Model):
    bus_name = models.CharField(max_length=30)
    source = models.CharField(max_length=30)
    dest = models.CharField(max_length=30)
    nos = models.IntegerField(default=0)
    rem = models.CharField(null=True, max_length=5)
    fare = models.CharField(null=True, max_length=6)
    date = models.DateField()
    time = models.TimeField()
    admin = models.ForeignKey(Admin,on_delete=models.CASCADE)
    

    def __str__(self):
        return self.bus_name
