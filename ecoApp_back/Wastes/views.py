from django.http import HttpResponse
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action

from Wastes.models import WasteSite, WasteTypes, WasteExample
from Wastes.serializer import WastSirtesSerializer, WastExampleSerializer, WasteTypesSerializer

class WastSitesViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset  = WasteSite.objects.all()
        serializer = WastSirtesSerializer(queryset, many=True)
        return Response(serializer.data)
    
    
class WasteExampleViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset  = WasteExample.objects.all()
        serializer = WastExampleSerializer(queryset, many=True)
        return Response(serializer.data)

class WasteTypesViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = WasteTypes.objects.all()
        serializer = WasteTypesSerializer
        return Response(serializer.data)