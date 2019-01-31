from rest_framework import serializers
from rest_framework.response import Response
from django.contrib.auth import authenticate, login, logout
from .models import *
from core.serializers import InstitutionSerializer
from core.models import Institution


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
    institution = InstitutionSerializer()

    class Meta:
        model = User
        fields = [
            'institution',
            'email',
            'contactNo',
            'chairperson',
            'chairpersonContact',
            'licenceNo',
            'password',
            'nameOfHOD'            
        ]
        read_only_fields = ['key']

    def create(self, validated_data):
       institution = validated_data['institution']
       del validated_data['institution']
       institutionData = Institution.objects.create(**institution)

       userData = User.objects.create(**validated_data)
       userData.institution = institutionData

       userData.save()
       return userData

class userSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ('password',)
