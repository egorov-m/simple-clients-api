from rest_framework.serializers import ListSerializer


class CustomListSerializer(ListSerializer):
    def to_representation(self, data):
        return data
