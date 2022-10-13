from dataclasses import fields
from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Location
from .models import WeatherAPI

class GetAllWeattherAPISerializer(serializers.ModelSerializer):
    class Meta:
        model=WeatherAPI
        fields=('Temperature','Windspeed','TrangThai','Id','LocationId','Date')

class WeatherAPISerializer(serializers.Serializer):
    Temperature1=serializers.IntegerField()
    Windspeed1=serializers.IntegerField()
    TrangThai1=serializers.CharField(max_length=12)
    Id1=serializers.IntegerField()
    LocationId1=serializers.IntegerField()
    Date1=serializers.CharField(max_length=12)

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

class GetLocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ['id', 'country', 'city']

class PostLocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ['country', 'city']
