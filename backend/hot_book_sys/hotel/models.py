from django.db import models
# from django_choices_field import TextChoicesField

# Create your models here.


class Hotel(models.Model):
    id = models.AutoField(primary_key=True)
    staff = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    floor = models.IntegerField()
    friendly_name = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    rating = models.FloatField(default=0.0)
    review_number = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class Room(models.Model):
    # hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    unique_identifier = models.IntegerField(default=0)
    floor = models.IntegerField()
    bed_number = models.IntegerField()
    room_number = models.IntegerField()
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    price_per_night = models.DecimalField(max_digits=10, decimal_places=2)
    capacity = models.IntegerField()

    def __str__(self):
        return self.name


class Booking(models.Model):

    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    check_in = models.DateField()
    check_out = models.DateField()
    guest_number = models.IntegerField()
    guest = models.CharField(max_length=100, default=0)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=(
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('cancelled', 'Cancelled'),
    ))
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.room.name} - {self.check_in} - {self.check_out}"

# tags
# if auth.user works, use it.
# create user auth for online and in-house bookings.
