from django.db import models

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
