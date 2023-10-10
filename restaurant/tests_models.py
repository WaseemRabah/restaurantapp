from django.test import TestCase
from django.contrib.auth.models import User
from .models import Booking, ContactMessage


class BookingModelTest(TestCase):
    def test_booking_creation(self):
        # Create a user
        user = User.objects.create(username='testuser')
        
        
        booking = Booking.objects.create(
            user=user,
            name='John Doe',
            email='johndoe@example.com',
            num_people=4,
            date='2023-10-15',
            time='18:00',
            occasion='1'
        )
        
        # Check if the booking was created successfully
        self.assertIsInstance(booking, Booking)
        self.assertEqual(booking.name, 'John Doe')
        self.assertEqual(booking.email, 'johndoe@example.com')
        self.assertEqual(booking.num_people, 4)
        self.assertEqual(booking.occasion, '1')

class ContactMessageModelTest(TestCase):
    def test_contact_message_creation(self):
        # Create a contact message
        contact_message = ContactMessage.objects.create(
            name='John Doe',
            email='johndoe@example.com',
            subject='Hello',
            message='This is a test message.'
        )
        
        # Check if the contact message was created successfully
        self.assertIsInstance(contact_message, ContactMessage)
        self.assertEqual(contact_message.name, 'John Doe')
        self.assertEqual(contact_message.email, 'johndoe@example.com')
        self.assertEqual(contact_message.subject, 'Hello')
        self.assertEqual(contact_message.message, 'This is a test message.')
