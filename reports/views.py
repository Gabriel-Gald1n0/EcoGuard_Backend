from reports.serializers import ReportSerializer
from reports.models import Report
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import AllowAny  # Permissão para acesso sem autenticação
from reports.permissions import IsReportCreator, ReadOnly

class ListCreateReportView(ListCreateAPIView):
    # Removendo a autenticação baseada em JWT
    # authentication_classes = [JWTAuthentication]
    
    # Permissão para qualquer usuário, sem autenticação
    permission_classes = [AllowAny]  # Ou, se desejar, pode usar IsAuthenticatedOrReadOnly
    queryset = Report.objects.all()
    serializer_class = ReportSerializer

    def perform_create(self, serializer):
        # Remover a associação com o usuário, já que não é mais necessário
        # serializer.save(user=self.request.user)
        serializer.save()

class RetrieveUpdateDestroyReportView(RetrieveUpdateDestroyAPIView):
    # Removendo a autenticação baseada em JWT
    # authentication_classes = [JWTAuthentication]
    
    # Permissão para qualquer usuário, sem autenticação
    permission_classes = [AllowAny]  # Ou outras permissões conforme sua necessidade
    queryset = Report.objects.all()
    serializer_class = ReportSerializer
    lookup_url_kwarg = 'report_id'
