import django_filters
from driverapp.models import Bus
from userapp.models import Book
from django_filters import DateFilter, CharFilter


class OrderFilter(django_filters.FilterSet):
    name=CharFilter(label= 'Drivers name')
    class Meta:
        model = Bus
        fields = ['bus_name' ,'source','destination','name']
        
class OrderFilterPassenger(django_filters.FilterSet):
    
    class Meta:
        model = Book
        fields = ['name']