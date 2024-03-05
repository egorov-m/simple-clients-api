from django.db import models

from .base import BaseModel


class Child(BaseModel):
    name = models.CharField(max_length=255, null=True, blank=True)
    surname = models.CharField(max_length=255, null=True, blank=True)
    patronymic = models.CharField(max_length=255, null=True, blank=True)
    dob = models.DateField(null=True, blank=True)
