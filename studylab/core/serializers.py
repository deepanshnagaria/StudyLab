from rest_framework import serializers
from .models import Institution

class InstitutionSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=40)
    headquarters = serializers.CharField(max_length=40)

    def create(self, validated_data):
        return Institution.objects.create(**validated_data)
