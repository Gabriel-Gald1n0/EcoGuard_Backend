from rest_framework.serializers import ModelSerializer
from regions.models import Region

class RegionSerializer(ModelSerializer):
    class Meta:
        model=Region
        fields="__all__"
        ref_name = 'RegionSerializer'
        
        