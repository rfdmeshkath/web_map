from rest_framework import serializers, exceptions
from django.contrib.auth import authenticate
from web_app import models


class UserSerializer(serializers.ModelSerializer):
    # database output serializer
    class Meta:
        fields = (
            'id',
            'username',
            'monitoring_station',
            'phone_number',
            'monitoring_time',
        )
        model = models.User


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()
    # validating if both the credentials are provided or not
    def validate(self, data):
        username = data.get('username', '')
        password = data.get('password', '')

        if username and password:
            user = authenticate(username=username, password=password)
            if user:
                data['user'] = user
            else:
                msg = 'unable to login with given given credentials'
                raise exceptions.ValidationError(msg)

        else:
            msg = 'Both username and password is required'
            raise exceptions.ValidationError(msg)
        return data