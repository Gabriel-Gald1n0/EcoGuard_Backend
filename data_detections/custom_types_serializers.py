from rest_framework import serializers
from custom_types.models import Custom_Type
from regions.models import Region
from arduinos.models import Arduino

class CustomTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Custom_Type
        fields = ['id', 'type']  # Inclui o id e o name

class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        ref_name = 'CustomTypeRegionSerializer'
        fields = ['id', 'street']  # Inclui o id e o street

class ArduinoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Arduino
        ref_name = 'CustomTypeArduinoSerializer'
        fields = ['id', 'name']  # Inclui o id e o name
