from simple_clients_api.core.serializers import PassportSerializer, ClientSerializer, AddressSerializer


def get_class_serializer_by_field_name(field_name: str):
    match field_name:
        case "passport":
            return PassportSerializer
        case "spouse":
            return ClientSerializer
        case _:
            return AddressSerializer
