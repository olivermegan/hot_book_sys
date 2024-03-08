import strawberry_django
from strawberry import auto
from . import models


@strawberry_django.type(models.Hotel)
class Hotel:
    name: auto
    id: auto
    description: auto
    floor: auto
    address: auto
    staff: auto
    country: auto
    rating: auto
    city: auto
    num_reviews: auto
    friendly_name: auto


# @strawberry_django.type(models.Room)
# class Room:
#     name: auto
#     id: auto
#     room_type: auto
#     room_status: auto
#     room_price: auto
#     room_image: auto
#     room_description: auto
#     room_capacity: auto
#     room_availability: auto
#     room_number: auto
#     room_floor: auto


# @strawberry_django.type(models.Booking)
# class Booking:
#     id: auto
#     room: auto
#     user: auto
#     check_in: auto
#     check_out: auto
#     total_price: auto
#     payment_status: auto
#     booking_status: auto
#     booking_date: auto
#     booking_time: auto
#     booking_number: auto
