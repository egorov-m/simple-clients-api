from rest_framework import serializers

from simple_clients_api.core import models


class CommunicationSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Communication
        fields = ("id", "type", "value")
