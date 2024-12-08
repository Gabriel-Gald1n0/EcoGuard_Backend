# soil_datas/views.py
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Soil_Data
from .serializers import SoilDataSerializer

class ListCreateSoilDataView(ListCreateAPIView):
    queryset = Soil_Data.objects.all()
    serializer_class = SoilDataSerializer

class RetrieveUpdateDestroySoilDataView(RetrieveUpdateDestroyAPIView):
    queryset = Soil_Data.objects.all()
    serializer_class = SoilDataSerializer
    lookup_url_kwarg = 'soil_data_id'
