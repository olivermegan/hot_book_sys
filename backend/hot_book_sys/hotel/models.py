from django.db import models

# Create your models here.
from django.db import models


class Hotel(models.Model):
    staff = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    floor = models.IntegerField()
    friendly_name = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    rating = models.FloatField(default=0.0)
    num_reviews = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class Room(models.Model):
    # hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    unique_identifier = models.IntegerField(default=0)
    floor = models.IntegerField()
    bed_number = models.IntegerField()
    room_number = models.IntegerField()
    # explicit_requirements =
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    price_per_night = models.DecimalField(max_digits=10, decimal_places=2)
    capacity = models.IntegerField()

    def __str__(self):
        return self.name
