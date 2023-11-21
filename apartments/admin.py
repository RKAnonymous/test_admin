from django.contrib import admin
from .models import Apartment, BookingApartment


admin.site.register(Apartment)
admin.site.register(BookingApartment)