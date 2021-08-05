from django.db import models
from adminapp.models import Admin,User
from driverapp.models import Bus

class User(models.Model):
    name = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    email = models.EmailField()
    
    def __str__(self):
        return self.email  



class Bus(models.Model):
    bus_name = models.CharField(max_length=30)
    source = models.CharField(max_length=100)
    dest = models.CharField(max_length=100)
    nos = models.IntegerField(default=0)
    rem = models.CharField(null=True, max_length=5)
    fare = models.CharField(null=True, max_length=6)
    date = models.DateField()
    time = models.TimeField()

    def __str__(self):
        return self.bus_name



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
<<<<<<< HEAD
    busid =models.ForeignKey(Bus, null=True,on_delete=models.CASCADE,)
    userid= models.ForeignKey(User,on_delete=models.CASCADE,null=True )
    dest = models.CharField(max_length=30,null=True ,blank=True)
=======
    admin_id =models.ForeignKey(Admin,null=True,on_delete=models.CASCADE, related_name='admin')
    # user = models.ForeignKey(User,on_delete=models.CASCADE)
    userid =models.ForeignKey(User,null=True,on_delete=models.CASCADE)
    busid=models.ForeignKey(Bus, null=True,on_delete=models.CASCADE)
    source = models.CharField(max_length=100, choices=SOURCE_CHOICES)
    dest = models.CharField(max_length=100,null=True ,blank=True, choices=DESTINATION_CHOICES)
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True )
    phone_number = models.IntegerField()
    destination = models.CharField(max_length=30,null=True ,blank=True, choices=DESTINATION_CHOICES)
>>>>>>> admin-views-forms
    seat_no = models.CharField(max_length=30,null=True)
    fare = models.CharField(null=True, max_length=6)
    date = models.DateField()
    time = models.TimeField()
    status = models.CharField(choices=TICKET_STATUSES, default=BOOKED, max_length=2)

    def __str__(self):
        return self.email

