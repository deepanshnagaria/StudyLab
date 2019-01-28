from rest_framework import serializers
from rest_framework.response import Response
from django.contrib.auth import authenticate, login, logout
from .models import *


class AuthTokenSerializer(serializers.Serializer):
    email = serializers.CharField(label="Email Address")
    password = serializers.CharField(label="Password", style={'input_type': 'password'})

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')

        user = authenticate(email=email, password=password)

        if user:
            if not user.is_active:
                msg = 'User account is disabled.'
                raise serializers.ValidationError(msg, code='authorization')
        else:
            raise AuthenticationFailed
        attrs['user'] = user
        return attrs

class CreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(required=True, style={'input_type': 'password'})

    class Meta:
        model = User
        fields = [
            'email',
            'password',
        ]
        read_only_fields = ['key']

class userSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ('password',)
