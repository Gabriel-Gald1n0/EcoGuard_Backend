# water_datas/views.py
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Water_Data
from .serializers import WaterDataSerializer

class ListCreateWaterDataView(ListCreateAPIView):
    queryset = Water_Data.objects.all()
    serializer_class = WaterDataSerializer

class RetrieveUpdateDestroyWaterDataView(RetrieveUpdateDestroyAPIView):
    queryset = Water_Data.objects.all()
    serializer_class = WaterDataSerializer
    lookup_url_kwarg = 'water_data_id'
