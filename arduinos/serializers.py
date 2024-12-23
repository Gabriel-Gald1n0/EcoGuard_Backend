from rest_framework.serializers import ModelSerializer
from arduinos.models import Arduino

class ArduinoSerializer(ModelSerializer):
    class Meta:
        model=Arduino
        fields="__all__"
        ref_name = 'ArduinoSerializer'
        
        