from rest_framework import serializers
from rest_framework.response import Response
from .models import *


class TestPapersSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestPapers
        fields = '__all__'

class TestSerializer(serializers.ModelSerializer):
    test = TestPapersSerializer()
    class Meta:
        model = Test
        fields =  [
            'name',
            'test'
        ]
    def create(self,validated_data):
        test = validated_data['test']
        del validated_data['test']
        test_temp = TestPapers.objects.create(
            **test
        )
        paper = Test.objects.create(**validated_data)
        paper.test = test_temp
        paper.save()
        return paper

class PaperSerializer(serializers.ModelSerializer):
    test = TestSerializer()
    class Meta:
        model = Paper
        fields = [
            'name',
            'date',
            'starttime',
            'duration',
            'uid',
            'test',
            'questions'
        ]
    
    def create(self,validated_data):
        testdata = validated_data['test']
        del validated_data['test']
        print(testdata)
        test_temp = Test.objects.create(
            **testdata
        )
        paper = Paper.objects.create(**validated_data)
        paper.testdata = test_temp
        paper.save()
        return paper
        

