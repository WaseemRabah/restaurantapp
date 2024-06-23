from django import forms
from .models import Booking, ContactMessage
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from datetime import date


class BookingForm(forms.ModelForm):
    date = forms.DateField(widget=forms.TextInput(attrs={'type': 'date'}))
    time = forms.TimeField(widget=forms.TextInput(attrs={'type': 'time'}))

    class Meta:
        model = Booking
        fields = ['name', 'email', 'num_people', 'date', 'time', 'occasion']

    def clean_date(self):
        selected_date = self.cleaned_data['date']
        if selected_date < date.today():
            raise forms.ValidationError("Cannot book a table in the past")
        return selected_date


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'subject', 'message']


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
