from django.shortcuts import render
from .models import Booking

# Create your views here.
def home(request):
    return render(request, 'home.html')


def booking_list(request):
    bookings = Booking.objects.all()
    return render(request, 'booking/booking_list.html', {'bookings': bookings})