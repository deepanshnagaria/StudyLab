from rest_framework import serializers
from .models import *

class InstitutionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Institution
        fields = '__all__'

class SubjectsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Subjects
        fields = "__all__"

class PhaseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Phase
        fields = "__all__"

# class StandardSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = Standards
