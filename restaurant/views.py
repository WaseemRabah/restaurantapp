from django.shortcuts import render, redirect, get_object_or_404
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


def booking_detail(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        bookings = Booking.objects.filter(email=email)
        return render(request, 'booking/booking_detail.html', {'bookings': bookings, 'email': email})
    else:
        return render(request, 'booking/email_input.html')


def delete_booking(request, pk):
    booking = get_object_or_404(Booking, pk=pk)

    

    if request.method == 'POST':
        
        booking.delete()
        return redirect('booking_list')  

    return render(request, 'booking/booking_confirm_delete.html', {'booking': booking})
