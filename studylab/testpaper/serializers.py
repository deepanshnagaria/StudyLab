from rest_framework import serializers
from rest_framework.response import Response
from .models import *


class TestPapersSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestPapers
        fields = '__all__'

class BatchesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Batches
        fields = '__all__'



class TestSerializer(serializers.ModelSerializer):
    testp = TestPapersSerializer()
    class Meta:
        model = Test
        fields =  [
            'name',
            'testp'
        ]
    def create(self,validated_data):
        test = validated_data['testp']
        print(validated_data)
        del validated_data['testp']
        test_temp = TestPapers.objects.create(
            **test
        )
        paper = Test.objects.create(**validated_data)
        paper.test = test_temp
        paper.save()
        return paper

class PaperSerializer(serializers.ModelSerializer):
    test = TestSerializer()
    batch = BatchesSerializer(many=True)
    # testpaper = TestPapersSerializer()
    class Meta:
        model = Paper
        fields = [
            'name',
            'date',
            'starttime',
            'endtime',
            'uid',
            'test',
            # 'testpaper',
            'questions',
            'type',
            'batch'
        ]
    
    def create(self,validated_data):
        
        testdata = validated_data['test']
        print(validated_data)


        
        testpaperdata = validated_data['test']['testp']
        print(testpaperdata)
        del validated_data['test']
        # del validated_data['testpaper']
        testpaper_temp = Test.TestPapers.objects.create(
            **testpaperdata
        )
        
        test_temp = Test.objects.create(
            **testdata
        )
        paper = Paper.objects.create(**validated_data)
        paper.testpaperdata = testpaper_temp
        paper.testdata = test_temp
        paper.save()
        return paper
        
class MarkingSchemeSerializer(serializers.ModelSerializer):
    paper = PaperSerializer()
    class Meta:
        model = Batches
        fields = [
            'question_type',
            'marksPositive',
            'marksNegative',
            'marksPerCorrect',
            'paper'
        ]
