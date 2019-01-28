from rest_framework import serializers
from .models import *

class CenterSerializer(serializers.ModelSerializer):
    # institution = serializers.StringRelatedField(many=True)

    class Meta:
        model = Center
        fields = "__all__"
