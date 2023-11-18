from rest_framework import routers

from Wastes.views import WastSitesViewSet, WasteExampleViewSet, WasteTypesViewSet

wastes_router = routers.SimpleRouter()
wastes_router.register(r'sites', WastSitesViewSet, basename="site")
wastes_router.register(r'examples', WasteExampleViewSet, basename="example")