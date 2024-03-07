from . import strawberry_django
from strawberry import auto
from . import models


@strawberry_django.type(models.Hotel)
class Hotel:
    name: auto
    id: auto
    hotel_type: auto
    hotel_status: auto
    hotel_price: auto
    hotel_image: auto
    hotel_description: auto
    hotel_capacity: auto
    hotel_availability: auto
    hotel_number: auto
    hotel_floor: auto
    hotel_address: auto
    hotel_phone: auto
    hotel_email: auto
    hotel_website: auto
    hotel_rating: auto
    hotel_reviews: auto
    hotel_latitude: auto
    hotel_longitude: auto
    hotel_location: auto
    hotel_amenities: auto
    hotel_facilities: auto
    hotel_parking: auto
    hotel_restaurants: auto
    hotel_transportation: auto
    hotel_attractions: auto
    hotel_sightseeing: auto
    hotel_shopping: auto
    hotel_culture: auto
    hotel_entertainment: auto
    hotel_food: auto
    hotel_drinks: auto
    hotel_dining: auto
    hotel_nightlife: auto


@strawberry_django.type(models.Room)
class Room:
    name: auto
    id: auto
    room_type: auto
    room_status: auto
    room_price: auto
    room_image: auto
    room_description: auto
    room_capacity: auto
    room_availability: auto
    room_number: auto
    room_floor: auto


@strawberry_django.type(models.Booking)
class Booking:
    id: auto
    room: auto
    user: auto
    check_in: auto
    check_out: auto
    total_price: auto
    payment_status: auto
    booking_status: auto
    booking_date: auto
    booking_time: auto
    booking_number: auto
