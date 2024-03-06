from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status, mixins
from rest_framework.decorators import action
from rest_framework.exceptions import NotFound
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.generics import get_object_or_404
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from simple_clients_api.core import models
from simple_clients_api.core.serializers import ClientWithSpouseSerializer
from simple_clients_api.utils.serializers import get_class_serializer_by_field_name

from simple_clients_api.utils.models import get_class_model_by_field_name

_search_fields = (
    "name",
    "surname",
    "patronymic",
    "passport__series"
)


class ClientViewSet(mixins.CreateModelMixin,
                    mixins.RetrieveModelMixin,
                    mixins.ListModelMixin,
                    GenericViewSet):
    queryset = models.ClientWithSpouse.objects.all()
    serializer_class = ClientWithSpouseSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter, SearchFilter]
    search_fields = _search_fields
    pagination_class = PageNumberPagination
    ordering_fields = ("createdAt", "updatedAt")

    @action(methods=["patch"], detail=False, url_path="<uuid:id>")
    def patch(self, request, pk=None):
        client = models.ClientWithSpouse.objects.filter(id=pk).first()
        if not client:
            raise NotFound

        serializer = self.serializer_class(client, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            for key, value in request.data.items():
                if key in ["passport", "living_address", "reg_address", "spouse"]:
                    class_nested_serializer = get_class_serializer_by_field_name(key)
                    if value is None:
                        setattr(client, key, None)
                    elif isinstance(value, dict):
                        nested_serializer = class_nested_serializer(data=value)
                        if nested_serializer.is_valid(raise_exception=True):
                            nested_instance = nested_serializer.save()
                            setattr(client, key, nested_instance)
                    elif isinstance(value, list):
                        for nested_data in value:
                            class_nested_model = get_class_model_by_field_name(key)
                            if "id" in nested_data:
                                nested_instance = get_object_or_404(class_nested_model, id=nested_data["id"])
                                nested_serializer = class_nested_serializer(instance=nested_instance, data=nested_data)
                            else:
                                nested_serializer = class_nested_serializer(data=nested_data)

                            if nested_serializer.is_valid(raise_exception=True):
                                nested_instance = nested_serializer.save()
                                getattr(client, key).add(nested_instance)
                else:
                    setattr(client, key, value)
                client.save()
            return Response(None, status=status.HTTP_204_NO_CONTENT)

    @action(methods=["delete"], detail=False, url_path="<uuid:id>")
    def delete(self, request, pk=None):
        client = models.ClientWithSpouse.objects.filter(id=pk).first()
        if not client:
            raise NotFound

        client.soft_deleted()
        return Response(None, status=status.HTTP_204_NO_CONTENT)
