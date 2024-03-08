import strawberry
from strawberry import field
from .models import Hotel, Room, Booking
from typing import List


def get_hotels():
    return Hotel.objects.all()


def get_rooms():
    return Room.objects.all()


def get_bookings():
    return Booking.objects.all()


@strawberry.type
class Query:
    hotels: List[Hotel] = field(resolver=get_hotels)
    rooms: List[Room] = field(resolver=get_rooms)
    bookings: List[Booking] = field(resolver=get_bookings)
