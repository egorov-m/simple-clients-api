from django.db import models

from .document import Document
from .address import Address
from .base import BaseModel, TimeStampedModel
from .child import Child
from .communication import Communication
from .job import Job
from .passport import Passport


class ClientWithSpouse(BaseModel, TimeStampedModel):
    name = models.CharField(max_length=255, null=True, blank=True)
    surname = models.CharField(max_length=255, null=True, blank=True)
    patronymic = models.CharField(max_length=255, null=True, blank=True)
    dob = models.DateField()
    passport = models.ForeignKey(Passport,
                                 related_name="client_passport",
                                 on_delete=models.SET_NULL,
                                 null=True,
                                 blank=True)
    living_address = models.ForeignKey(Address,
                                       related_name="client_living_address",
                                       on_delete=models.SET_NULL,
                                       null=True,
                                       blank=True)
    reg_address = models.ForeignKey(Address,
                                    related_name="client_reg_address",
                                    on_delete=models.SET_NULL,
                                    null=True,
                                    blank=True)
    cur_work_exp = models.DecimalField(max_digits=3, decimal_places=3, null=True, blank=True, editable=False)
    type_education = models.CharField(max_length=20,
                                      choices=[("secondary", "Среднее"), ("secondarySpecial", "Среднее специальное"),
                                               ("incompleteHigher", "Незаконченное высшее"), ("higher", "Высшее"),
                                               ("twoOrMoreHigher", "Два и более высших образований"),
                                               ("academicDegree", "Академическая степень")],
                                      null=True,
                                      blank=True)
    mon_income = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True)
    mon_expenses = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True)
    spouse = models.ForeignKey("ClientWithSpouse",
                               related_name="client_spouse",
                               on_delete=models.SET_NULL,
                               null=True,
                               blank=True)


class ChildClient(BaseModel):
    client = models.ForeignKey(ClientWithSpouse, on_delete=models.CASCADE)
    child = models.ForeignKey(Child, on_delete=models.CASCADE)


class DocumentClient(BaseModel):
    client = models.ForeignKey(ClientWithSpouse, on_delete=models.CASCADE)
    document = models.ForeignKey(Document, on_delete=models.CASCADE)


class JobClient(BaseModel):
    client = models.ForeignKey(ClientWithSpouse, on_delete=models.CASCADE)
    job = models.ForeignKey(Job, on_delete=models.CASCADE)


class CommunicationClient(BaseModel):
    client = models.ForeignKey(ClientWithSpouse, on_delete=models.CASCADE)
    communication = models.ForeignKey(Communication, on_delete=models.CASCADE)
