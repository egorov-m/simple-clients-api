from django.db import models

from .base import BaseModel, TimeStampedModel


class Address(BaseModel, TimeStampedModel):
    zip_code = models.CharField(max_length=10, null=True, blank=True)
    country = models.CharField(max_length=255, null=True, blank=True)
    region = models.CharField(max_length=255, null=True, blank=True)
    city = models.CharField(max_length=255, null=True, blank=True)
    street = models.CharField(max_length=255, null=True, blank=True)
    house = models.CharField(max_length=255, null=True, blank=True)
    apartment = models.CharField(max_length=255, null=True, blank=True)
