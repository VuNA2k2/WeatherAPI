from django.contrib import admin
from .models import Location, WeatherAPI
# Register your models here.
admin.site.register(WeatherAPI)
admin.site.register(Location)
