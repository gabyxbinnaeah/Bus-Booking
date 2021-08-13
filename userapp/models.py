from django.db import models
from multiselectfield import MultiSelectField
from django.contrib.auth.models import User
from django.db import models
from adminapp.models import Admin
from driverapp.models import Bus



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
    source = models.CharField(max_length=30)
    destination = models.CharField(max_length=30,null=True ,blank=True)
    fare = models.CharField(null=True, max_length=6)
    date = models.DateField(null=True)
    time = models.TimeField(null=True)
    status = models.CharField(choices=TICKET_STATUSES, default=BOOKED, max_length=2)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    seat_no = MultiSelectField(max_length=200,null=True,choices=SEAT_OPTIONS)
    checked_seats= models.CharField(max_length=2)


    @classmethod
    def show_bookings(cls,email):
        booking=cls.objects.filter(email=email)
        return booking
        
    @classmethod
    def search_passengers(cls,passenger):
        search = cls.objects.filter(name__icontains=passenger)
        return search

    def __str__(self):
        return self.email



class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        abstract = True
        
# M-pesa Payment models
class MpesaCalls(BaseModel):
    ip_address = models.TextField()
    caller = models.TextField()
    conversation_id = models.TextField()
    content = models.TextField()
    class Meta:
        verbose_name = 'Mpesa Call'
        verbose_name_plural = 'Mpesa Calls'
class MpesaCallBacks(BaseModel):
    ip_address = models.TextField()
    caller = models.TextField()
    conversation_id = models.TextField()
    content = models.TextField()
    class Meta:
        verbose_name = 'Mpesa Call Back'
        verbose_name_plural = 'Mpesa Call Backs'
class MpesaPayment(BaseModel):
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    type = models.TextField()
    reference = models.TextField()
    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone_number = models.TextField()
    organization_balance = models.DecimalField(max_digits=10, decimal_places=2)
    class Meta:
        verbose_name = 'Mpesa Payment'
        verbose_name_plural = 'Mpesa Payments'
    def __str__(self):
        return self.first_name

class  Fare(models.Model):
    phone_number=models.IntegerField() 
    fare=models.DecimalField(max_digits=6, decimal_places=2)

    
    

 

