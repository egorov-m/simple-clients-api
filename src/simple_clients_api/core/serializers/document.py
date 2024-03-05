from rest_framework import serializers

from simple_clients_api.core import models


class DocumentSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Document
        fields = (
            "id",
        )
