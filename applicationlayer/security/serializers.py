from rest_framework import serializers
from entities import models
from datetime import datetime

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=15)
    password = serializers.CharField(max_length=50)


class CurrentUserContextSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=255)
    email = serializers.CharField(max_length=255)
    firstname = serializers.CharField(max_length=255)
    middlename = serializers.CharField(max_length=255)
    lastname = serializers.CharField(max_length=255)
    birthdate = serializers.CharField(max_length=255)
    is_administrator = serializers.BooleanField()
