from django.db import models
import datetime
from django.core.exceptions import ValidationError


# Create your models here.

class User(models.Model):
    full_name = models.CharField(max_length=255, unique=True)
    email = models.EmailField(max_length=255, unique=True)
    birth_date = models.DateField()

    def __str__(self):
        return self.full_name + ' --- ' + str(self.birth_date)

    def save(self, *args, **kwargs):
        if self.birth_date > datetime.date.today():
            raise ValidationError("The date cannot be in the future!")
        super(User, self).save(*args, **kwargs)
