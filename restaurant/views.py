from django.shortcuts import render, redirect, get_object_or_404
from .models import Booking
from .forms import BookingForm, ContactForm, CreateUserForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


# Create your views here.
def home(request):
    return render(request, 'home.html')

def menu(request):
    return render(request, 'menu.html')


def registerPage(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user=form.cleaned_data.get('username')
            messages.success(request, 'Account was created for ' + user)
            return redirect('login')

    context = {'form':form}
    return render(request, 'accounts/register.html', context)


def loginPage(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Username or Password is incorrect')
            

    context = {}
    return render(request, 'accounts/login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('login')

@login_required
def booking_list(request):
    bookings = Booking.objects.filter(user=request.user)
    return render(request, 'booking/booking_list.html', {'bookings': bookings})

@login_required
def create_booking(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            booking.save()
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

@login_required
def booking_detail(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        bookings = Booking.objects.filter(user=request.user, email=email)
        return render(request, 'booking/booking_detail.html', {'bookings': bookings, 'email': email})
    else:
        return render(request, 'booking/email_input.html')


def delete_booking(request, pk):
    booking = get_object_or_404(Booking, pk=pk)

    

    if request.method == 'POST':
        
        booking.delete()
        return redirect('booking_list')  

    return render(request, 'booking/booking_confirm_delete.html', {'booking': booking})


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            
            return redirect('contact_thank_you')  
    else:
        form = ContactForm()
    
    return render(request, 'contact.html', {'form': form})


def contact_thank_you(request):
    return render(request, 'contact_thank_you.html')
