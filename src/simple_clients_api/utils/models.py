from simple_clients_api.core.models import Passport, ClientWithSpouse, Address


def get_class_model_by_field_name(field_name: str):
    match field_name:
        case "passport":
            return Passport
        case "spouse":
            return ClientWithSpouse
        case _:
            return Address
