from dataclasses import fields
from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Location


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