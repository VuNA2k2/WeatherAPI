
from django.db import models

# Create your models here.

class WeatherAPI(models.Model):
    Temperature=models.IntegerField(default=0)
    Windspeed=models.IntegerField(default=0)
    TrangThai=models.CharField(max_length=255)
    Id=models.IntegerField(default=0)
    LocationId=models.IntegerField(default=0)
    Date=models.CharField(max_length=255)
    
class Location(models.Model):
    id = models.AutoField(primary_key=True)
    country = models.CharField("Country", max_length=30)
    city = models.CharField("City", max_length=30)
