# air_datas/serializers.py
from rest_framework import serializers
from .models import Air_Data

class AirDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Air_Data
        fields = '__all__'  # Ou defina explicitamente os campos que deseja incluir
