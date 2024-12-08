# air_datas/urls.py
from django.urls import path
from .views import ListCreateAirDataView, RetrieveUpdateDestroyAirDataView

urlpatterns = [
    path('air_data/', ListCreateAirDataView.as_view(), name='list-create-air-data'),
    path('air_data/<int:air_data_id>/', RetrieveUpdateDestroyAirDataView.as_view(), name='retrieve-update-destroy-air-data'),
]
