from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import ugettext_lazy as _
from django.conf import settings
from core.models import Institution
from django.core.validators import MaxValueValidator

class UserManager(BaseUserManager):
    def create_user(self, email, password,  **extra_fields):
        if not email:
            raise ValueError('Enter email')

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        user = self.create_user(email, password, **extra_fields)
        user.is_superuser = True
        user.is_active = True
        user.is_staff = True
        user.save()
        return user

class User(AbstractBaseUser, PermissionsMixin):
    email               = models.EmailField(_('email address'), unique=True)
    nameOfHOD           = models.CharField(_('Name Of HOD'),max_length=40)
    instituteName       = models.CharField(_('Institute Name'),max_length=40)
    contactNo           = models.PositiveIntegerField(validators=[MaxValueValidator(9999999999)],blank=True,null=True,unique=True)
    headquarters        = models.CharField(_('Headquarters'),max_length=40)
    chairperson         = models.CharField(_('Chairperson Name'),max_length=40,unique=True)
    chairpersonContact  = models.PositiveIntegerField(validators=[MaxValueValidator(9999999999)],blank=True,null=True,unique=True)
    date_joined         = models.DateTimeField(_('date joined'), auto_now_add=True)
    is_active           = models.BooleanField(_('active'), default=True)
    licenceNo           = models.CharField(_('Licence No.'),max_length=40,unique=True)


    is_staff = models.BooleanField(
        verbose_name='Staff Status',
        default=False,
        help_text='Check if is staff ',
    )

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

class Course(models.Model):
    slug = models.SlugField(max_length=100)
    name = models.CharField(max_length=100)
    tutor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
