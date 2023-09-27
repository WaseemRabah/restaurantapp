from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),  
    path('booking_list/', views.booking_list, name='booking_list'),  
    path('create_booking/', views.create_booking, name='create_booking'),  
    path('update_booking/<int:pk>/', views.update_booking, name='update_booking'),
    path('delete_booking/<int:pk>/', views.delete_booking, name='delete_booking'),
    path('booking_detail/', views.booking_detail, name='booking_detail'),
    path('contact/', views.contact, name='contact'),
    path('contact_thank_you/', views.contact_thank_you, name='contact_thank_you'),
]