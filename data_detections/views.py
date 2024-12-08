from data_detections.serializers import Data_DetectionSerializer
from data_detections.models import Data_Detection
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import AllowAny  # Permissão para acesso sem autenticação
from arduinos.models import Arduino
from django.shortcuts import get_object_or_404
import re

class ListCreateData_DetectionView(ListCreateAPIView):
    # Removendo a autenticação baseada em JWT
    # authentication_classes = [JWTAuthentication]
    
    # Permissão para qualquer usuário, sem autenticação
    permission_classes = [AllowAny]  # Ou, se desejar, pode usar IsAuthenticatedOrReadOnly
    queryset = Data_Detection.objects.all()
    serializer_class = Data_DetectionSerializer

    def perform_create(self, serializer):
        # Associando ao Arduino sem precisar de autenticação de usuário
        arduino_id = int(re.search(r'\d+', self.request.path_info).group())
        arduino = get_object_or_404(Arduino, id=arduino_id)
        serializer.save(arduino=arduino)

class RetrieveUpdateDestroyData_DetectionView(RetrieveUpdateDestroyAPIView):
    # Removendo a autenticação baseada em JWT
    # authentication_classes = [JWTAuthentication]
    
    # Permissão para qualquer usuário, sem autenticação
    permission_classes = [AllowAny]  # Ou outras permissões conforme sua necessidade
    queryset = Data_Detection.objects.all()
    serializer_class = Data_DetectionSerializer
    lookup_url_kwarg = 'arduino_id'
