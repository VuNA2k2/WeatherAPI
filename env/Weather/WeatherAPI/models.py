
from django.db import models

# Create your models here.
class WeatherAPI(models.Model):
    temperature=models.IntegerField("Temperature",default=0)
    wind_speed=models.IntegerField("Wind_speed",default=0)
    trang_thai=models.CharField("Trang_thai",max_length=30)
    id=models.AutoField(primary_key=True)
    location_id=models.IntegerField("Location_Id",default=0)
    date=models.CharField("Date",max_length=30)
        
class Location(models.Model):
    id = models.AutoField(primary_key=True)
    country = models.CharField("Country", max_length=30)
    city = models.CharField("City", max_length=30)
