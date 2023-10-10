from django.test import TestCase
from .forms import BookingForm, ContactForm, CreateUserForm

class BookingFormTest(TestCase):

    def test_booking_form_valid(self):
        data = {
            'name': 'John Doe',
            'email': 'johndoe@example.com',
            'num_people': 4,
            'date': '2023-10-15',
            'time': '18:00',
            'occasion': '4'
        }
        form = BookingForm(data=data)
        if not form.is_valid():
            print(form.errors)
        self.assertTrue(form.is_valid())




class ContactFormTest(TestCase):

    def test_contact_form_valid(self):
        data = {
            'name': 'John Doe',
            'email': 'johndoe@example.com',
            'subject': 'Hello',
            'message': 'This is a test message.'
        }
        form = ContactForm(data=data)
        self.assertTrue(form.is_valid())



class CreateUserFormTest(TestCase):

    def test_create_user_form_valid(self):
        data = {
            'username': 'testuser',
            'email': 'testuser@example.com',
            'password1': 'testpassword123',
            'password2': 'testpassword123'
        }
        form = CreateUserForm(data=data)
        self.assertTrue(form.is_valid())

    
