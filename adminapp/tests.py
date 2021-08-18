from django.test import TestCase
from adminapp.models import Book,Bus,Admin
# Create your tests here.
class BookTestClass(TestCase):
    #setup method
    def setUp(self):
        self.book1=Book(
            name="group1",
            email='group1@gmail.com',
            source="Nairobi",
            dest="Kericho",
            fare="2000",
            date="2021-08-12",
            time="13:00",
            status="2",
          
            seat_no="12",
           
        )

    #Testing Instance
    def test_instance(self):
        self.assertTrue(isinstance(self.book1,Book))

    def test_save_booking(self):
        self.book1.save_booking()
        book=Book.objects.all()
        self.assertTrue(len(book)>0)

    def test_delete_booking(self):
        self.book1.save_booking()
        book_record=Book.objects.all()
        self.book1.delete_booking()
        self.assertTrue(len(book_record)==0)

    def test_update_booking(self):
        book=Book.objects.first()
        new_book=Book.update_booking()
        expected_book=f'{new_book}'
        self.assertTrue(expected_book,'new_book')

class BusTestClass(TestCase):
    #setup method
    def setUp(self):
        self.bus1=Bus(
            bus_name="simba",
            source="Nairobi",
            dest="Kericho",
            fare="2000",
            date="2021-08-12",
            time="13:00",
            nos="12",
            rem="2",
            

        )

    #Testing Instance
    def test_instance(self):
        self.assertTrue(isinstance(self.bus1,Bus))

    def test_save_bus(self):
        self.bus1.save_bus()
        bus=Bus.objects.all()
        self.assertTrue(len(bus)>0)

    def test_delete_bus(self):
        self.bus1.save_bus()
        bus_record=Bus.objects.all()
        self.bus1.delete_bus()
        self.assertTrue(len(bus_record)==0)

    def test_update_bus(self):
        bus=Bus.objects.first()
        new_bus=Bus.update_bus()
        expected_bus=f'{new_bus}'
        self.assertTrue(expected_bus,'new_bus')

class AdminTestClass(TestCase):
    #setup method
    def setUp(self):
        self.admin1=Admin(
            name="admin1",
            email='admin1@gmail.com',
            password="password",
           
            
        )

    #Testing Instance
    def test_instance(self):
        self.assertTrue(isinstance(self.admin1,Admin))

    def test_save_admin(self):
        self.admin1.save_admin()
        admin=Admin.objects.all()
        self.assertTrue(len(admin)>0)

    def test_delete_admin(self):
        self.admin1.save_admin()
        admin_record=Admin.objects.all()
        self.admin1.delete_admin()
        self.assertTrue(len(admin_record)==0)

    def test_update_admin(self):
        admin=Admin.objects.first()
        new_admin=Admin.update_admin()
        expected_admin=f'{new_admin}'
        self.assertTrue(expected_admin,'new_admin')