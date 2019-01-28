from django.db import models
from core.models import *
from datetime import datetime, timedelta

class Center(models.Model):

    institution = models.ForeignKey(
            Institution,
            on_delete = models.CASCADE
            )
    name = models.CharField(max_length=40, verbose_name="center name")
    address = models.CharField(max_length=60, verbose_name="address")
    hod = models.CharField(max_length=40, verbose_name="hod")
    contact = models.CharField(max_length=10, verbose_name="contact")
    def __str__(self):
        return self.name

class Batch(models.Model):

    institution = models.ForeignKey(
            Institution,
            on_delete = models.CASCADE
            )
    phase = models.ForeignKey(
            Phase,
            on_delete = models.CASCADE
            )
    name = models.CharField(max_length=40, verbose_name="batch name")
    
    def __str__(self):
        return self.name

class Classes(models.Model):

    center = models.ForeignKey(
            Center,
            on_delete = models.CASCADE
            )
    phase = models.ForeignKey(
            Phase,
            on_delete = models.CASCADE
            )
    batch = models.ForeignKey(
            Batch,
            on_delete = models.CASCADE
            )

    def __str__(self):
        return self.center.name

class SubjectClasses(models.Model):
    classes = models.ForeignKey(
            Classes,
            on_delete = models.CASCADE
            )
    subjects = models.ForeignKey(
            Subjects,
            on_delete = models.CASCADE
            )

    def __str__(self):
        return str(self.classes)
