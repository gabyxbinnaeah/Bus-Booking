from django.test import TestCase
from driverapp.models import Bus,Book,Driver

# Create your tests here.
class BookTestClass(TestCase):
    #setup method
    def setUp(self):
        self.book1=Book(
            name="group1",
            email='group1@gmail.com',
            source="Nairobi",
            destination="Kericho",
            fare="2000",
            date="2021-08-12",
            time="13:00",
            status="2",
            created_at="2021-08-12",
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
            destination="Kericho",
            fare="2000",
            date="2021-08-12",
            time="13:00",
            nos="12",
            rem="2",
            name="Driver",
            email="d@gmail.com",
            password="nairobi",
            Contact="0705952719"

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


class DriverTestClass(TestCase):
    #setup method
    def setUp(self):
        self.driver1=Driver(
            name="group1",
            email='group1@gmail.com',
            password="password",
            Contact="0700987654"
            
        )

    #Testing Instance
    def test_instance(self):
        self.assertTrue(isinstance(self.driver1,Driver))

    def test_save_driver(self):
        self.driver1.save_driver()
        driver=Driver.objects.all()
        self.assertTrue(len(driver)>0)

    def test_delete_driver(self):
        self.driver1.save_driver()
        driver_record=Driver.objects.all()
        self.driver1.delete_driver()
        self.assertTrue(len(driver_record)==0)

    def test_update_driver(self):
        driver=Driver.objects.first()
        new_driver=Driver.update_driver()
        expected_driver=f'{new_driver}'
        self.assertTrue(expected_driver,'new_driver')
