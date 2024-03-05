from rest_framework import serializers

from simple_clients_api.core import models


class PassportSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Passport
        fields = (
            "id",
            "series",
            "number",
            "giver",
            "date_issued",
            "created_at",
            "updated_at"
        )
