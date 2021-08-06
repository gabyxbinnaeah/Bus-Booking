from django.db import models
from django.contrib.auth.models import User
from adminapp.models import Admin
from driverapp.models import Bus
from django.db import models

# Create your models here.
class BusCategory(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    
    def __str__(self):
        return self.email  

class Book(models.Model):
    DESTINATION_CHOICES = (
        ('nairobi','Nairobi'),
        ('nakuru','Nakuru'),
        ('kericho','Kericho'),
    )
    SOURCE_CHOICES=(
        ('kitale','Kitale'),
        ('eldoret','Eldoret'),
        ('kisumu','Kisumu'),
    )



    BOOKED = 'B'
    CANCELLED = 'C'

    TICKET_STATUSES = ((BOOKED, 'Booked'),
                       (CANCELLED, 'Cancelled'),)
    email = models.EmailField()
    name = models.CharField(max_length=30)
    admin_id =models.ForeignKey(Admin,null=True,on_delete=models.CASCADE, related_name='admin')
    userid =models.ForeignKey(User,null=True,on_delete=models.CASCADE)
    busid=models.ForeignKey(Bus, null=True,on_delete=models.CASCADE)
    source = models.CharField(max_length=100, choices=SOURCE_CHOICES)
    phone_number = models.IntegerField(null=True, blank=True)
    destination = models.CharField(max_length=30,null=True ,blank=True, choices=DESTINATION_CHOICES)
    seat_no = models.CharField(max_length=30,null=True)
    number_of_Seats = models.IntegerField(default=0) 
    fare = models.CharField(null=True, max_length=6)
    date = models.DateField()
    time = models.TimeField()
    status = models.CharField(choices=TICKET_STATUSES, default=BOOKED, max_length=2)

    def __str__(self):
        return self.email

