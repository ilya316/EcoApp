from rest_framework import routers

from .views import UserViewSet

auth_router = routers.SimpleRouter()
auth_router.register(r'user', UserViewSet, basename="user")