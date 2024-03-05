from django.db import models

from .address import Address
from .base import BaseModel, TimeStampedModel


class Job(BaseModel, TimeStampedModel):
    type = models.CharField(max_length=20,
                            choices=[
                                ("main", "Основная работа"),
                                ("part-time", "Частичная занятость")
                            ],
                            null=True,
                            blank=True)
    date_emp = models.DateField(null=True, blank=True)
    date_dismissal = models.DateField(null=True, blank=True)
    mon_income = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True)
    tin = models.CharField(max_length=12, null=True, blank=True)
    fact_address = models.ForeignKey(Address,
                                     related_name="job_fact_address",
                                     on_delete=models.CASCADE,
                                     null=True,
                                     blank=True)
    jur_address = models.ForeignKey(Address,
                                    related_name="job_jur_address",
                                    on_delete=models.CASCADE,
                                    null=True,
                                    blank=True)
    phone_number = models.CharField(max_length=20, null=True, blank=True)
