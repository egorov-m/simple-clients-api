from rest_framework import serializers

from simple_clients_api.core import models


class AddressSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Address
        fields = (
            "id",
            "zip_code",
            "country",
            "region",
            "city",
            "street",
            "house",
            "apartment",
            "created_at",
            "updated_at"
        )
