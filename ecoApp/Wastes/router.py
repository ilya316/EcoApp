from rest_framework import routers

from Wastes.views import WastSitesViewSet

router = routers.SimpleRouter()
router.register(r'wasts', WastSitesViewSet, basename="wastes")