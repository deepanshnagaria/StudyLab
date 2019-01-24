from django.db import models
from core.models import *
from django.contrib.postgres.fields import ArrayField
from jsonfield import JSONField
#from django_mysql.models import JSONField

class Data(models.Model):
    institute               = models.OneToOneField(
        Institution,
        on_delete=models.CASCADE

    )
    verbose_name = str(institute.name) + '_data'

class Dpp(models.Model):
    name                    = models.CharField(
        max_length=40,
    )

    
    questions               = ArrayField(JSONField())

    data                    = models.ForeignKey(
        Data,
        on_delete=models.CASCADE
    )
    phase                   = models.ForeignKey(
        Phase,
        on_delete=models.CASCADE
    )

    subjects                = models.ForeignKey(
        Subjects,
        on_delete=models.CASCADE
    )

    standard                = models.ForeignKey(
        Standards,
        on_delete=models.CASCADE
    )


class Test(models.Model):
    name=models.CharField(max_length=50)
    data                    = models.ForeignKey(
        Data,
        on_delete=models.CASCADE
    )
    phase                   = models.ForeignKey(
        Phase,
        on_delete=models.CASCADE
    )

    standard                = models.ForeignKey(
        Standards,
        on_delete=models.CASCADE
    )

    questions               = ArrayField(JSONField(null=True, blank=True),blank=True,)

class Booklet(models.Model):
    name=models.CharField(max_length=50)
    data                    = models.ForeignKey(
        Data,
        on_delete=models.CASCADE
    )
    phase                   = models.ForeignKey(
        Phase,
        on_delete=models.CASCADE
    )

    subjects                = models.ForeignKey(
        Subjects,
        on_delete=models.CASCADE
    )

    standard                = models.ForeignKey(
        Standards,
        on_delete=models.CASCADE
    )

    questions               = ArrayField(JSONField())