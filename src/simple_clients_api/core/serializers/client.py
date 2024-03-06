from rest_framework import serializers

from .base import CustomListSerializer
from .. import models
from .address import AddressSerializer
from .child import ChildSerializer
from .communication import CommunicationSerializer
from .job import JobSerializer
from .passport import PassportSerializer


class ClientSerializer(serializers.ModelSerializer):
    children = ChildSerializer(many=True, allow_null=True, default=[])

    document_ids = serializers.PrimaryKeyRelatedField(queryset=models.Document.objects.all(), allow_null=True, default=[])

    passport = PassportSerializer(allow_null=False, default=None)
    living_address = AddressSerializer(allow_null=False, default=None)
    reg_address = AddressSerializer(allow_null=False, default=None)
    jobs = JobSerializer(many=True, allow_null=True, default=[])
    communications = CommunicationSerializer(many=True, allow_null=True, default=[])

    class Meta:
        model = models.ClientWithSpouse
        list_serializer_class = CustomListSerializer
        fields = (
            "id",
            "name",
            "surname",
            "patronymic",
            "dob",
            "children",
            "document_ids",
            "passport",
            "living_address",
            "reg_address",
            "jobs",
            "cur_work_exp",
            "type_education",
            "mon_income",
            "mon_expenses",
            "communications",
            "created_at",
            "updated_at"
        )


class ClientWithSpouseSerializer(ClientSerializer):
    spouse = ClientSerializer(allow_null=False, default=None)

    class Meta:
        model = models.ClientWithSpouse
        fields = (*ClientSerializer.Meta.fields, "spouse")
