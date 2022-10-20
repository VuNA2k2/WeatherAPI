from dataclasses import fields
from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Location, Weather

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
class GetWeatherSerializer(serializers.ModelSerializer):
    class Meta:
        model=Weather
        fields=('temperature','wind_speed','status','id','location_id','date')

class PostWeatherSerializer(serializers.ModelSerializer):
    class Meta:
        model=Weather
        fields=('temperature','wind_speed','status','location_id','date')