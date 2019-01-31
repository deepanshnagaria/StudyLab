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
    test                = models.ForeignKey(TestPapers,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
    
class Paper(models.Model):
    name                = models.CharField(_('Paper Name'),max_length=40)  
    date                = models.DateField(auto_now=False,auto_now_add=False)
    starttime           = models.TimeField()
    duration            = models.TimeField()
    uid                 = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    test                = models.ForeignKey(Test,on_delete=models.CASCADE)
    questions           = models.TextField()

    def __str__(self):
        return self.name
       
    
