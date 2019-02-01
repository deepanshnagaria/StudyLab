from django.db import models
from Institution.models import *
from django.utils.translation import ugettext_lazy as _
import uuid

class TestPapers(models.Model):
    center              = models.ForeignKey(Center,on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.center)

class Test(models.Model):
    name                = models.CharField(_('Test Name'),max_length=40)
    testp               = models.ForeignKey(TestPapers,on_delete=models.CASCADE,related_name='testpapers')
    
    def __str__(self):
        return self.name
    
class Batches(models.Model):
    batchName           = models.CharField(max_length=40)

    def __str__(self):
        return self.batchName
    


class Paper(models.Model):
    TYPE = (
        ('DPP','DPP'),
        ('TES','TEST')
    )
    name                = models.CharField(_('Paper Name'),max_length=40)  
    date                = models.DateField(auto_now=False,auto_now_add=False)
    starttime           = models.TimeField()
    endtime             = models.TimeField()
    uid                 = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    test                = models.ForeignKey(Test,on_delete=models.CASCADE,related_name='test')
    questions           = models.TextField()
    type                = models.CharField(choices=TYPE,max_length=4,default='DPP')
    batch               = models.ManyToManyField(Batches)
    


    def __str__(self):
        return self.name
       
    
class MarkingScheme(models.Model):
    QUESTION_TYPES = (
        ('MULTMCQ','Multicorrect MCQ'),
        ('PARA','Paragraph'),
        ('SINGMCQ','Singlecorrect MCQ'),
        ('MATCH','Matrix Match'),
    )
    question_type       = models.CharField(max_length=40,choices = QUESTION_TYPES)
    marksPositive       = models.IntegerField()
    marksNegative       = models.IntegerField()
    marksPerCorrect     = models.IntegerField()
    paper               = models.ForeignKey(Paper,on_delete=models.CASCADE,related_name='paper_name')

    def __str__(self):
        return str(self.paper)
    