# imoveis/urls.py

from django.urls import path
from . import views
from .views import ImovelCreateView, ImovelDetailView, ImovelUpdateView # 🌟 Adicione ImovelUpdateView

urlpatterns = [
    # Rota principal (Lista de imóveis)
    path('', views.lista_imoveis, name='lista_imoveis'),
    
    # Rota de Cadastro
    path('cadastro/', ImovelCreateView.as_view(), name='cadastro_imovel'), 
    
    # Rota de Detalhes
    path('<int:pk>/', ImovelDetailView.as_view(), name='detalhe_imovel'), 
    
    # 🌟 NOVA ROTA: Edição de Imóvel
    # Precisa do pk (ID) para saber qual imóvel editar
    path('<int:pk>/editar/', ImovelUpdateView.as_view(), name='editar_imovel'), 
]