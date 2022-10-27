from dataclasses import fields
from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Location, Weather


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password',
                  'email', 'first_name', 'last_name')
        write_only_fields = ('password',)
        read_only_fields = ('id',)


class EditUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password',
                  'email', 'first_name', 'last_name')
        write_only_fields = ('password',)
        read_only_fields = ('id', 'username')


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
        model = Weather
        fields = ('temperature', 'wind_speed', 'status',
                  'id', 'location_id', 'date', 'humidity')


class PostWeatherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Weather
        fields = ('temperature', 'wind_speed', 'status',
                  'location_id', 'date', 'humidity')
