# imoveis/admin.py
from django.contrib import admin
from .models import Imovel, ImagemImovel # 🌟 Importar o novo modelo



# 1. Define o estilo de formulário inline (para fotos)
class ImagemImovelInline(admin.TabularInline):
    model = ImagemImovel
    extra = 1 # Número de formulários vazios para adicionar de uma
    
    
# ==============================================================================
# CLASSE DE ADMINISTRAÇÃO PERSONALIZADA
# ==============================================================================
@admin.register(Imovel)
class ImovelAdmin(admin.ModelAdmin):
    # Campos que serão exibidos na lista principal de imóveis no painel do Admin
    list_display = ('titulo', 'preco', 'tipo', 'esta_a_venda', 'data_criacao')
    
    # Adiciona filtros laterais para facilitar a organização
    list_filter = ('tipo', 'esta_a_venda')
    
    # Adiciona campos de pesquisa rápida
    search_fields = ('titulo', 'endereco')
    
    # Permite editar o status de venda diretamente na lista (True/False)
    list_editable = ('esta_a_venda',) 
    
    # Ordem padrão na listagem
    ordering = ('-data_criacao',) 
    
    # 🌟 Adiciona o Inline à página de edição do Imóvel
    inlines = [ImagemImovelInline]
    
    # Opcional: Define a ordem e aparência dos campos no formulário de edição/criação
    fieldsets = (
        (None, {
            'fields': ('titulo', 'descricao', 'preco', 'endereco', 'tipo')
        }),
        ('Status', {
            'fields': ('esta_a_venda',),
        }),
    )

# A linha '@admin.register(Imovel)' é a mesma que usar:
# admin.site.register(Imovel, ImovelAdmin)