import uuid

from django.db import models


class BaseModel(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)

    class Meta:
        abstract = True


class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, null=False, editable=False)
    updated_at = models.DateTimeField(auto_now=True, null=False, editable=False)

    class Meta:
        abstract = True
