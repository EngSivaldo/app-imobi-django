# imoveis/forms.py

from django import forms
from .models import Imovel

# Usamos ModelForm para criar um formulário automaticamente
# com base no nosso modelo Imovel
class ImovelForm(forms.ModelForm):
    
    # A classe Meta é onde definimos as opções do nosso ModelForm
    class Meta:
        model = Imovel # O modelo que queremos usar
        # Quais campos do modelo Imovel devem aparecer no formulário?
        fields = (
            'titulo', 'descricao', 'preco', 'endereco', 
            'tipo', 'esta_a_venda'
        ) 

        # Opcional: Adicionar labels mais amigáveis
        labels = {
            'titulo': 'Título do Anúncio',
            'preco': 'Preço (€)',
            'endereco': 'Morada',
            'tipo': 'Tipo de Imóvel',
            'esta_a_venda': 'Disponível para Venda?',
        }

        # Opcional: Adicionar classes Bootstrap/Tailwind para estilização
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'descricao': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'preco': forms.NumberInput(attrs={'class': 'form-control'}),
            'endereco': forms.TextInput(attrs={'class': 'form-control'}),
            # O campo 'tipo' e 'esta_a_venda' usam widgets padrão de seleção e checkbox
        }
        
        
        
# imoveis/forms.py (Dentro da classe ImovelForm)

class ImovelForm(forms.ModelForm):
    class Meta:
        model = Imovel
        # Adicione o campo 'imagem_principal' aqui!
        fields = (
            'titulo', 'descricao', 'preco', 'endereco', 
            'tipo', 'esta_a_venda', 'imagem_principal' 
        ) 

        labels = {
            # ... labels existentes ...
            'imagem_principal': 'Foto de Capa do Imóvel',
        }
        
        widgets = {
            # ... widgets existentes ...
            # Não precisamos de widget especial para ImageField
        }