from rest_framework import serializers

from Wastes.models import WasteSite

class WastSirtesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = WasteSite
        fields = ['name', 'address', 'yard_type', 'lattitude', 'longitude']