from rest_framework import serializers

from .. import models
from .address import AddressSerializer


class JobSerializer(serializers.ModelSerializer):
    fact_address = AddressSerializer(required=False)
    jur_address = AddressSerializer(required=False)

    class Meta:
        model = models.Job
        fields = (
            "id",
            "type",
            "date_emp",
            "date_dismissal",
            "mon_income",
            "tin",
            "fact_address",
            "jur_address",
            "phone_number",
            "created_at",
            "updated_at"
        )
