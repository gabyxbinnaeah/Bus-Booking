from django.test import TestCase
from userapp.models import Book,BaseModel,MpesaCallBacks,MpesaCalls,MpesaPayment,Fare

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
            checked_seats="2"
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

class MpesacallsTestClass(TestCase):
    #setup method
    def setUp(self):
        self.payment1=MpesaCalls(
            ip_address="168.154.87.2",
            caller="mpesa",
            conversation_id="message",
            content="content"
            
        )

    #Testing Instance
    def test_instance(self):
        self.assertTrue(isinstance(self.payment1,MpesaCalls))

    def test_save_mpesacalls(self):
        self.payment1.save_call()
        date=MpesaCalls.objects.all()
        self.assertTrue(len(date)>0)

class MpesacallbacksTestClass(TestCase):
    #setup method
    def setUp(self):
        self.payment1=MpesaCallBacks(
            ip_address="168.154.87.2",
            caller="mpesa",
            conversation_id="message",
            content="content"
            
        )

    #Testing Instance
    def test_instance(self):
        self.assertTrue(isinstance(self.payment1,MpesaCallBacks))

    def test_save_mpesacallbacks(self):
        self.payment1.save_callback()
        date=MpesaCallBacks.objects.all()
        self.assertTrue(len(date)>0)

class Mpesapayment(TestCase):
    #setup method
    def setUp(self):
        self.payment1=MpesaPayment(
            amount="1500",
            description="confirmed",
            type="send money",
            reference="company name",
            first_name="senders first name",
            middle_name="senders middle name",
            last_name="senders last name",
            phone_number="0789876543",
            organization_balance="10000"
        )

    #Testing Instance
    def test_instance(self):
        self.assertTrue(isinstance(self.payment1,MpesaPayment))

    def test_save_mpayment(self):
        self.payment1.save_payment()
        date=MpesaPayment.objects.all()
        self.assertTrue(len(date)>0)

class BasemodelTestClass(TestCase):
    #setup method
    def setUp(self):
        self.payment1=BaseModel(
            
            created_at="2021-08-12",
            updated_at="2021-08-12"
        )

    #Testing Instance
    def test_instance(self):
        self.assertTrue(isinstance(self.payment1,BaseModel))

    # def test_save_basemodel(self):
    #     self.payment1.save_date()
    #     date=BaseModel.objects.all()
    #     self.assertTrue(len(date)>0)