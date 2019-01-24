from django.db import models
from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.core.validators import RegexValidator
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class Standards(models.Model):
    STANDARD_TYPE= (
            ('11th','11th'),
            ('12th','12th'),
            ('13th','13th'),
            )
    standard_type = models.CharField(choices=STANDARD_TYPE, max_length=10, verbose_name = 'standard type')

    def __str__(self):
        return self.standard_type

class Institution(models.Model):
    name                = models.CharField(max_length=40)
    headquarters        = models.CharField(max_length=40)

    def __str__(self):
        return self.name

class Subjects(models.Model):
    SUBJECTS_TYPE = (
        ('PHY','Physics'),
        ('CHEM','Chemistry'),
        ('MATH','Maths'),
        ('BIOL','Biology')
    )
    LANGUAGES = (
        ('HIN','Hindi'),
        ('ENG','English'),
    )
    subject            = models.CharField(
        max_length=20, 
        choices=SUBJECTS_TYPE,
        verbose_name='Subjects'
    )
    language            = models.CharField(
        max_length=20,
        choices = LANGUAGES,
        verbose_name = 'Language',
    )
    def __str__(self):
        return self.subject
