from django.db import models
from adminapp.models import Admin
from driverapp.models import Bus

# Create your models here.
class Book(models.Model):
    BOOKED = 'B'
    CANCELLED = 'C'

    TICKET_STATUSES = ((BOOKED, 'Booked'),
                       (CANCELLED, 'Cancelled'),)
    email = models.EmailField()
    name = models.CharField(max_length=30)
    admin_id =models.ForeignKey(Admin,null=True,on_delete=models.CASCADE, related_name='admin')
    bus_id =models.ForeignKey(Bus, null=True,on_delete=models.CASCADE)
    # user = models.ForeignKey(User,on_delete=models.CASCADE)
    source = models.CharField(max_length=30)
    dest = models.CharField(max_length=30,null=True ,blank=True)
    seat_no = models.CharField(max_length=30,null=True)
    fare = models.CharField(null=True, max_length=6)
    date = models.DateField()
    time = models.TimeField()
    status = models.CharField(choices=TICKET_STATUSES, default=BOOKED, max_length=2)

    def __str__(self):
        return self.email