from . models import Hotel
from . models import Room
from . models import Booking


def get_hotels():
    return Hotel.objects.all()


def get_rooms():
    return Room.objects.all()


def get_bookings():
    return Booking.objects.all()
