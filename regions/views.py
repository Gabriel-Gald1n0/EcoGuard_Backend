from regions.serializers import RegionSerializer
from regions.models import Region
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import AllowAny  # Permissão para acesso sem autenticação
from regions.permissions import IsRegionCreator, ReadOnly

class ListCreateRegionView(ListCreateAPIView):
    # Removendo a autenticação baseada em JWT
    # authentication_classes = [JWTAuthentication]
    
    # Permissão para qualquer usuário, sem autenticação
    permission_classes = [AllowAny]  # Ou, se desejar, pode usar IsAuthenticatedOrReadOnly
    queryset = Region.objects.all()
    serializer_class = RegionSerializer

    def perform_create(self, serializer):
        # Remover a associação com o usuário, já que não é mais necessário
        # serializer.save(user=self.request.user)
        serializer.save()

class RetrieveUpdateDestroyRegionView(RetrieveUpdateDestroyAPIView):
    # Removendo a autenticação baseada em JWT
    # authentication_classes = [JWTAuthentication]
    
    # Permissão para qualquer usuário, sem autenticação
    permission_classes = [AllowAny]  # Ou outras permissões conforme sua necessidade
    queryset = Region.objects.all()
    serializer_class = RegionSerializer
    lookup_url_kwarg = 'region_id'
