from rest_framework.serializers import ModelSerializer
from data_detections.models import Data_Detection
from .custom_types_serializers import CustomTypeSerializer, RegionSerializer, ArduinoSerializer

class Data_DetectionSerializer(ModelSerializer):
    type = CustomTypeSerializer()  # Inclui os dados de Custom_Type
    region = RegionSerializer()  # Inclui os dados de Region
    arduino = ArduinoSerializer()  # Inclui os dados de Arduino

    class Meta:
        model = Data_Detection
        fields = '__all__'  # Inclui todos os campos do modelo
        extra_kwargs = {
            "arduino": {"read_only": True}  # Tornando o campo arduino somente leitura
        }
