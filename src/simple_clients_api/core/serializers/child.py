from rest_framework import serializers

from simple_clients_api.core import models


class ChildSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Child
        fields = (
            "id",
            "name",
            "surname",
            "patronymic",
            "dob"
        )
