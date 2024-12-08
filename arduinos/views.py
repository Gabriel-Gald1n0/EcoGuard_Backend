from arduinos.serializers import ArduinoSerializer
from arduinos.models import Arduino
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import AllowAny  # Permissão para permitir acesso sem autenticação

class ListCreateArduinoView(ListCreateAPIView):
    # Removendo a autenticação baseada em JWT
    # authentication_classes = [JWTAuthentication]
    
    # Permissão para qualquer usuário, sem precisar de autenticação
    permission_classes = [AllowAny]
    queryset = Arduino.objects.all()
    serializer_class = ArduinoSerializer

    def perform_create(self, serializer):
        # Se você não deseja associar o usuário com o Arduino, pode remover a linha abaixo
        # serializer.save(user=self.request.user)
        serializer.save()

class RetrieveUpdateDestroyArduinoView(RetrieveUpdateDestroyAPIView):
    # Removendo a autenticação baseada em JWT
    # authentication_classes = [JWTAuthentication]
    
    # Permissão para qualquer usuário, sem precisar de autenticação
    permission_classes = [AllowAny]  # Ou outras permissões personalizadas, se necessário
    queryset = Arduino.objects.all()
    serializer_class = ArduinoSerializer
    lookup_url_kwarg = 'arduino_id'
