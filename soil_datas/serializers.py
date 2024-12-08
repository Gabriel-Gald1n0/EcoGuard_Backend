# soil_datas/serializers.py
from rest_framework import serializers
from .models import Soil_Data

class SoilDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Soil_Data
        fields = '__all__'  # Ou defina explicitamente os campos que deseja incluir
