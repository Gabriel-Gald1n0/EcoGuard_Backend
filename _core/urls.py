"""
URL configuration for _core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

# Configuração do esquema para o Swagger
schema_view = get_schema_view(
    openapi.Info(
        title="Sua API",
        default_version="v1",
        description="Documentação da API do seu projeto",
        terms_of_service="https://www.seusite.com/termos/",
        contact=openapi.Contact(email="contato@seusite.com"),
        license=openapi.License(name="Licença BSD"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include("users.urls")),
    path('api/', include("arduinos.urls")),
    path('api/', include("regions.urls")),
    path('api/', include("reports.urls")),
    path('api/', include("custom_types.urls")),
    path('api/', include("data_detections.urls")),
    path('api/soil/', include('soil_datas.urls')),
    path('api/water/', include('water_datas.urls')),
    path('api/air/', include('air_datas.urls')),

     # Adicione o endpoint do Swagger
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
