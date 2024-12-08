# water_datas/urls.py
from django.urls import path
from .views import ListCreateWaterDataView, RetrieveUpdateDestroyWaterDataView

urlpatterns = [
    path('water_data/', ListCreateWaterDataView.as_view(), name='list-create-water-data'),
    path('water_data/<int:water_data_id>/', RetrieveUpdateDestroyWaterDataView.as_view(), name='retrieve-update-destroy-water-data'),
]
