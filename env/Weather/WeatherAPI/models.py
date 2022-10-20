import datetime
from django.db import models

# Create your models here.
class Location(models.Model):
    id = models.AutoField(primary_key=True)
    country = models.CharField("Country", max_length=30)
    city = models.CharField("City", max_length=30)

class Weather(models.Model):
    temperature=models.IntegerField()
    wind_speed=models.IntegerField()
    status=models.CharField(max_length=30)
    id=models.AutoField(primary_key=True)
    location_id=models.IntegerField()
    date=models.DateField()