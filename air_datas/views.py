# air_datas/views.py
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Air_Data
from .serializers import AirDataSerializer

class ListCreateAirDataView(ListCreateAPIView):
    queryset = Air_Data.objects.all()
    serializer_class = AirDataSerializer

class RetrieveUpdateDestroyAirDataView(RetrieveUpdateDestroyAPIView):
    queryset = Air_Data.objects.all()
    serializer_class = AirDataSerializer
    lookup_url_kwarg = 'air_data_id'
