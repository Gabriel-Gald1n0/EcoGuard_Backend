from rest_framework import serializers  # Importando o módulo serializers corretamente
from rest_framework.serializers import ModelSerializer
from reports.models import Report


class ReportSerializer(ModelSerializer):
    
    class Meta:
        model = Report
        fields = "__all__"
