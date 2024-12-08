# soil_datas/urls.py
from django.urls import path
from .views import ListCreateSoilDataView, RetrieveUpdateDestroySoilDataView

urlpatterns = [
    path('soil_data/', ListCreateSoilDataView.as_view(), name='list-create-soil-data'),
    path('soil_data/<int:soil_data_id>/', RetrieveUpdateDestroySoilDataView.as_view(), name='retrieve-update-destroy-soil-data'),
]
