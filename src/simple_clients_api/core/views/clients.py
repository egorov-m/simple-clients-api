from uuid import UUID

from rest_framework.response import Response
from rest_framework.views import APIView

from simple_clients_api.core.serializers import ClientSerializer, ClientWithSpouseSerializer


class ClientsView(APIView):
    serializer_class = ClientSerializer

    def get(self, request):
        return Response()

    def post(self, request):
        return Response()


class ClientsByIdView(APIView):
    serializer_class = ClientWithSpouseSerializer

    def get(self, request, client_id: UUID):
        return Response()

    def patch(self, request, client_id: UUID):
        return Response()

    def delete(self, request, client_id: UUID):
        return Response()
