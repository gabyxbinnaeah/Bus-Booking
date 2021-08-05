from django.db import models

# Create your models here.
class Driver(models.Model):
    name = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    email = models.EmailField()
    contact= models.CharField(max_length=30)
    
    def __str__(self):
        return self.email
    
    @classmethod
    def Driver(cls):
        drivers = cls.objects.all()
        return drivers

    def save_driver(self):
        self.save()

    def delete_driver(self):
        self.delete() 
    
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

    def __str__(self):
        return self.bus_name
    
    @classmethod
    def Bus(cls):
        buses = cls.objects.all()
        return buses


    def save_bus(self):
        self.save()

    def delete_bus(self):
        self.delete()
    
    # @classmethod
    # def search_bus(cls, name):
    #     return cls.objects.filter(user__username__icontains=name).all()




class Book(models.Model):
    BOOKED = 'B'
    CANCELLED = 'C'

    TICKET_STATUSES = ((BOOKED, 'Booked'),
                       (CANCELLED, 'Cancelled'),)
    email = models.EmailField()
    name = models.CharField(max_length=30)
    userid =models.ForeignKey(Driver,null=True,on_delete=models.CASCADE)
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