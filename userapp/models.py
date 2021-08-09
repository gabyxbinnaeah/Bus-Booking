from django.db import models
from multiselectfield import MultiSelectField

SEAT_OPTIONS = (
            (1, "1"),
            (2, "2"),
            (4, "4"),
            (5, "5"),
            (6, "6"),
            (7, "7"),
            (8, "8"),
            (9, "9"),
            (10, "10"),
            (11, "11"),
            (12, "12"),
            (13, "13"),
            (14, "14"),
            (15, "15"),
            (16, "16"),
            (17, "17"),
            (18, "18"),
            (19, "19"),
            (20, "20"),
            (21, "21"),
            (22, "22"),
            (23, "23"),
            (24, "24"),
            (25, "25"),
        )
from django.contrib.auth.models import User

# Create your models here.
from django.db import models

# Create your models here.
class BusCategory(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Bus(models.Model):
    bus_category = models.ForeignKey(BusCategory,on_delete=models.CASCADE,default='')
    bus_name = models.CharField(max_length=30)
    source = models.CharField(max_length=30)
    destination = models.CharField(max_length=30)
    nos = models.IntegerField(default=0)
    rem = models.CharField(null=True, max_length=5)
    fare = models.CharField(null=True, max_length=6)
    date = models.DateField()
    time = models.TimeField()

    def __str__(self):
        return self.bus_name



class Book(models.Model):
    BOOKED = 'B'
    CANCELLED = 'C'

    TICKET_STATUSES = ((BOOKED, 'Booked'),
                       (CANCELLED, 'Cancelled'),)
    email = models.EmailField()
    name = models.CharField(max_length=30)
    source = models.CharField(max_length=30)
    dest = models.CharField(max_length=30,null=True ,blank=True)
    seat_no = MultiSelectField(max_length=200,null=True,choices=SEAT_OPTIONS)
    fare = models.CharField(null=True, max_length=6)
    date = models.DateField(null=True)
    time = models.TimeField(null=True)
    checked_seats= models.CharField(max_length=2)
    status = models.CharField(choices=TICKET_STATUSES, default=BOOKED, max_length=2)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    userid =models.ForeignKey(User,null=True,on_delete=models.CASCADE)
    busid=models.ForeignKey(Bus, null=True,on_delete=models.CASCADE)

    def __str__(self):
        return self.email
        
