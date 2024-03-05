from django.db import models

from .base import BaseModel


class Communication(BaseModel):
    type = models.CharField(max_length=5, choices=[
        ("email", "Электронная почта"),
        ("phone", "Мобильный телефон"),
    ])
    value = models.CharField(max_length=20)
