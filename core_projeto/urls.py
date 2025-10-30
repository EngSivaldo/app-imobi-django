# core_projeto/urls.py

from django.contrib import admin
from django.urls import path, include 

# 🌟 Importações necessárias para servir arquivos media
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    # 🌟 NOVAS ROTAS DE AUTENTICAÇÃO DO DJANGO
    # Mapeia as views de login, logout, password change, etc.
    path('', include('django.contrib.auth.urls')),
    
    path('', include('imoveis.urls')), 
]

# 🌟 Configuração para servir arquivos de media (só funciona em DEBUG=True)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)