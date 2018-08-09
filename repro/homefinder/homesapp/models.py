from django.db import models

# Create your models here.

class Location(models.Model):
    location_name = models.CharField(max_length = 200) # Name of location
    location_type = models.CharField(max_length = 200) # Type of location

class Property(models.Model):
    location = models.ForeignKey(Location, on_delete = models.CASCADE)
    property_name = models.CharField(max_length = 200)
    area = models.CharField(max_length = 200)

    