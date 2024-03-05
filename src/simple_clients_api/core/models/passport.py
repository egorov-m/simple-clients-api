from django.db import models

from .base import BaseModel, TimeStampedModel


class Passport(BaseModel, TimeStampedModel):
    series = models.CharField(max_length=10)
    number = models.CharField(max_length=20)
    giver = models.CharField(max_length=255)
    date_issued = models.DateField()
