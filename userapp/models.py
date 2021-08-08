from django.db import models
from multiselectfield import MultiSelectField


class User(models.Model):
    name = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    email = models.EmailField()
    
    def _str_(self):
        return self.email  


class Bus(models.Model):
    bus_name = models.CharField(max_length=30)
    source = models.CharField(max_length=30)
    dest = models.CharField(max_length=30)
    nos = models.IntegerField(default=0)
    fare = models.CharField(null=True, max_length=6)
    date = models.DateField()

    def _str_(self):
        return self.bus_name
    
    @classmethod
    def search_buses(cls, source, dest):
        return cls.objects.filter(source_icontains=source , dest_icontains=dest).all()



class Book(models.Model):
    BOOKED = 'B'
    CANCELLED = 'C'

    TICKET_STATUSES = ((BOOKED, 'Booked'),
                       (CANCELLED, 'Cancelled'),)

    SEAT_CHOICES =(
            ("Seat1", "Seat1"),
            ("Seat2", "Seat2"),
            ("Seat4", "Seat4"),
            ("Seat5", "Seat5"),
            ("Seat6", "Seat6"),
            ("Seat7", "Seat7"),
            ("Seat8", "Seat8"),
            ("Seat9", "Seat9"),
            ("Seat10", "Seat10"),
            ("Seat11", "Seat11"),
            ("Seat12", "Seat12"),
            ("Seat13", "Seat13"),
            ("Seat14", "Seat14"),
            ("Seat15", "Seat15"),
            ("Seat16", "Seat16"),
            ("Seat17", "Seat17"),
            ("Seat18", "Seat18"),
            ("Seat19", "Seat19"),
            ("Seat20", "Seat20"),
            ("Seat21", "Seat21"),
            ("Seat3", "Seat3"),
            ("Seat3", "Seat3"),
            ("Seat3", "Seat3")
        )

    email = models.EmailField()
    name = models.CharField(max_length=30)
    userid =models.ForeignKey(User,null=True,on_delete=models.CASCADE)
    busid=models.ForeignKey(Bus, null=True,on_delete=models.CASCADE)
    source = models.CharField(max_length=30)
    dest = models.CharField(max_length=30,null=True ,blank=True)
    seat_no = MultiSelectField(max_length=30,choices=SEAT_CHOICES, null=True)
    fare = models.CharField(null=True, max_length=6)
    date = models.DateField()
    time = models.TimeField()
    status = models.CharField(choices=TICKET_STATUSES, default=BOOKED, max_length=2)

    def _str_(self):
        return self.email