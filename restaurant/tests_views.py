from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Booking, ContactMessage
from .forms import BookingForm, ContactForm, CreateUserForm

class TestHomeView(TestCase):
    def test_home_view(self):
        # Test the home view
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')

class TestMenuView(TestCase):
    def test_menu_view(self):
        # Test the menu view
        response = self.client.get(reverse('menu'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'menu.html')

class TestRegisterPageView(TestCase):
    def test_register_page_view(self):
        # Test the register page view
        response = self.client.get(reverse('register'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/register.html')

class TestLoginPageView(TestCase):
    def test_login_page_view(self):
        # Test the login page view
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/login.html')

class TestLogoutUserView(TestCase):
    def test_logout_user_view(self):
        # Test the logout user view
        response = self.client.get(reverse('logout'))
        self.assertRedirects(response, '/login/')

class TestBookingListView(TestCase):
    def setUp(self):
        
        self.user = User.objects.create_user(username='testuser', password='testpassword')

    def test_booking_list_view_authenticated(self):
        # Test the booking list view for an authenticated user
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('booking_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'booking/booking_list.html')

    def test_booking_list_view_unauthenticated(self):
        # Test the booking list view for an unauthenticated user (should redirect to login)
        response = self.client.get(reverse('booking_list'))
        self.assertRedirects(response, '/login/?next=/booking_list/')

class TestCreateBookingView(TestCase):
    def setUp(self):
        
        self.user = User.objects.create_user(username='testuser', password='testpassword')

    def test_create_booking_view_authenticated(self):
        # Test the create booking view for an authenticated user
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('create_booking'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'booking/booking_form.html')

    def test_create_booking_view_unauthenticated(self):
        # Test the create booking view for an unauthenticated user (should redirect to login)
        response = self.client.get(reverse('create_booking'))
        self.assertRedirects(response, '/login/?next=/create_booking/')

class TestUpdateBookingView(TestCase):
    def setUp(self):
        
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        
        self.booking = Booking.objects.create(
            user=self.user,
            name='John Doe',
            email='johndoe@example.com',
            num_people=4,
            date='2023-10-15',
            time='18:00',
            occasion='1'
        )

    def test_update_booking_view_authenticated(self):
        # Test the update booking view for an authenticated user
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('update_booking', args=[self.booking.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'booking/booking_form.html')


class TestBookingDetailView(TestCase):
    def setUp(self):
        
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        
        self.booking = Booking.objects.create(
            user=self.user,
            name='John Doe',
            email='johndoe@example.com',
            num_people=4,
            date='2023-10-15',
            time='18:00',
            occasion='1'
        )

    def test_booking_detail_view_authenticated(self):
        # Test the booking detail view for an authenticated user
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('booking_detail'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'booking/email_input.html')

class TestDeleteBookingView(TestCase):
    def setUp(self):
        
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        
        self.booking = Booking.objects.create(
            user=self.user,
            name='John Doe',
            email='johndoe@example.com',
            num_people=4,
            date='2023-10-15',
            time='18:00',
            occasion='1'
        )


class TestContactView(TestCase):
    def test_contact_view(self):
        # Test the contact view
        response = self.client.get(reverse('contact'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'contact.html')

class TestContactThankYouView(TestCase):
    def test_contact_thank_you_view(self):
        # Test the contact thank you view
        response = self.client.get(reverse('contact_thank_you'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'contact_thank_you.html')
