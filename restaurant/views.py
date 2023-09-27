from django.shortcuts import render, redirect
from .models import Booking
from .forms import BookingForm

# Create your views here.
def home(request):
    return render(request, 'home.html')


def booking_list(request):
    bookings = Booking.objects.all()
    return render(request, 'booking/booking_list.html', {'bookings': bookings})


def create_booking(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('booking_list')
    else:
        form = BookingForm()
    return render(request, 'booking/booking_form.html', {'form': form})


def update_booking(request, pk):
    booking = Booking.objects.get(pk=pk)
    if request.method == 'POST':
        form = BookingForm(request.POST, instance=booking)
        if form.is_valid():
            form.save()
            return redirect('booking_list')
    else:
        form = BookingForm(instance=booking)
    return render(request, 'booking/booking_form.html', {'form': form})