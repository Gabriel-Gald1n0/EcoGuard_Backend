from custom_types.serializers import Custom_TypeSerializer
from custom_types.models import Custom_Type
from water_datas.models import Water_Data  # Adicione as importações necessárias
from soil_datas.models import Soil_Data    # Adicione as importações necessárias
from air_datas.models import Air_Data      # Adicione as importações necessárias
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import AllowAny  # Permissão para acesso sem autenticação

class ListCreateCustom_TypeView(ListCreateAPIView):
    # Removendo a autenticação baseada em JWT
    # authentication_classes = [JWTAuthentication]
    
    # Permissão para qualquer usuário, sem autenticação
    permission_classes = [AllowAny]
    
    queryset = Custom_Type.objects.all()
    serializer_class = Custom_TypeSerializer

    def perform_create(self, serializer):
        # Obtém o tipo escolhido (Water, Soil ou Air)
        type_choice = self.request.data.get("name")
        
        if type_choice == "Water":
            # Recupera o dado relacionado à água (WaterData)
            water = Water_Data.objects.get(id=self.request.data["water"])
            serializer.save(water=water)
        elif type_choice == "Soil":
            # Recupera o dado relacionado ao solo (SoilData)
            soil = Soil_Data.objects.get(id=self.request.data["soil"])
            serializer.save(soil=soil)
        elif type_choice == "Air":
            # Recupera o dado relacionado ao ar (AirData)
            air = Air_Data.objects.get(id=self.request.data["air"])
            serializer.save(air=air)
        else:
            # Caso não seja nenhum dos tipos definidos, apenas salva normalmente
            serializer.save()

class RetrieveUpdateDestroyCustom_TypeView(RetrieveUpdateDestroyAPIView):
    # Removendo a autenticação baseada em JWT
    # authentication_classes = [JWTAuthentication]
    
    # Permissão para qualquer usuário, sem autenticação
    permission_classes = [AllowAny]
    
    queryset = Custom_Type.objects.all()
    serializer_class = Custom_TypeSerializer
    lookup_url_kwarg = 'type_id'
