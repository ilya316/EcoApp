from rest_framework import routers

from Wastes.views import WastSitesViewSet, WasteExampleViewSet

wast_site_router = routers.SimpleRouter()
wast_site_router.register(r'wast_sites', WastSitesViewSet, basename="site")

wast_example_router = routers.SimpleRouter()
wast_example_router.register(r'wast_examples', WasteExampleViewSet, basename="example")