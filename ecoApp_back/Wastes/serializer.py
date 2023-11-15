from rest_framework import serializers

from Wastes.models import WasteSite, WasteTypes, WasteExample

class WasteTypesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = WasteTypes
        fields = ['type', 'description', 'yard_type']

class WastSirtesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = WasteSite
        fields = ['name', 'address', 'yard_type', 'lattitude', 'longitude']
        
class WastExampleSerializer(serializers.HyperlinkedModelSerializer):
    waste_type = WasteTypesSerializer()
    
    class Meta:
        model = WasteExample
        fields = ['name', 'description', 'waste_type']