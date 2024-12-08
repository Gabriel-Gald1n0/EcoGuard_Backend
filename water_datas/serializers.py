# water_datas/serializers.py
from rest_framework import serializers
from .models import Water_Data

class WaterDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Water_Data
        fields = '__all__'  # Ou defina explicitamente os campos que deseja incluir
