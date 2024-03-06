from django.contrib import admin
from django.urls import path
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from rest_framework import routers

from simple_clients_api.core.views.clients import ClientsByIdView, ClientViewSet

router = routers.DefaultRouter()

urlpatterns = router.urls

urlpatterns += [
    path("clients/", ClientViewSet.as_view({"get": "list", "post": "create"})),
    path("clients/<uuid:client_id>/", ClientsByIdView.as_view()),
    path("admin/", admin.site.urls),
    path("openapi.yaml", SpectacularAPIView.as_view(), name="schema"),
    path("docs/", SpectacularSwaggerView.as_view(url_name="schema")),
]
