# imoveis/views.py

from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.forms.models import inlineformset_factory

from .models import Imovel, ImagemImovel
from .forms import ImovelForm


# ==============================================================================
# CONFIGURAÇÃO DO FORMSET PARA MÚLTIPLAS IMAGENS
# ==============================================================================
ImagemFormSet = inlineformset_factory(
    Imovel,              # Modelo Pai
    ImagemImovel,        # Modelo Filho (as fotos)
    fields=('imagem', 'descricao'), 
    extra=3,             
    can_delete=True      
)

# ==============================================================================
# VIEW: Lista de Imóveis (Página Inicial) - FBV
# ==============================================================================
def lista_imoveis(request):
    """
    Busca todos os imóveis ativos no banco de dados e os exibe 
    na página inicial do catálogo.
    """
    imoveis_disponiveis = Imovel.objects.filter(esta_a_venda=True).order_by('-data_criacao')
    
    contexto = {
        'imoveis': imoveis_disponiveis,
        'titulo_pagina': 'Catálogo de Imóveis e Lotes',
    }
    
    return render(request, 'imoveis/lista_imoveis.html', contexto)


# ==============================================================================
# VIEW: Detalhe do Imóvel (DetailView) - CBV
# ==============================================================================
class ImovelDetailView(DetailView):
    model = Imovel # 🌟 Propriedade obrigatória
    template_name = 'imoveis/detalhe_imovel.html' 
    context_object_name = 'imovel'


# ==============================================================================
# VIEW: Cadastro de Novo Imóvel (CreateView) - CBV
# ==============================================================================
class ImovelCreateView(CreateView):
    model = Imovel # 🌟 Propriedade obrigatória
    form_class = ImovelForm # 🌟 Propriedade obrigatória
    template_name = 'imoveis/cadastro_imovel.html' 
    success_url = reverse_lazy('lista_imoveis')

    # Passa e carrega o Formset
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.POST:
            context['galeria_formset'] = ImagemFormSet(self.request.POST, self.request.FILES)
        else:
            context['galeria_formset'] = ImagemFormSet()
        return context

    # Valida e Salva o Formset
    def form_valid(self, form):
        
        context = self.get_context_data()
        galeria_formset = context['galeria_formset']

        if galeria_formset.is_valid():
            self.object = form.save()
            galeria_formset.instance = self.object
            galeria_formset.save()
            return super().form_valid(form)
        else:
            return self.render_to_response(self.get_context_data(form=form))


# ==============================================================================
# VIEW: Edição de Imóvel (UpdateView) - CBV
# ==============================================================================
class ImovelUpdateView(UpdateView):
    model = Imovel # 🌟 CORRIGIDO: Propriedade obrigatória
    form_class = ImovelForm # 🌟 CORRIGIDO: Propriedade obrigatória
    template_name = 'imoveis/cadastro_imovel.html' # 🌟 CORRIGIDO: Propriedade obrigatória

    # Passa e carrega o Formset (com dados existentes)
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.POST:
            context['galeria_formset'] = ImagemFormSet(self.request.POST, self.request.FILES, instance=self.object)
        else:
            context['galeria_formset'] = ImagemFormSet(instance=self.object)
        return context
    
    # Valida e Salva o Formset
    def form_valid(self, form):
        context = self.get_context_data()
        galeria_formset = context['galeria_formset']
        
        if galeria_formset.is_valid():
            response = super().form_valid(form)
            galeria_formset.instance = self.object
            galeria_formset.save()
            return response
        else:
            return self.render_to_response(self.get_context_data(form=form))

    # Define para onde redirecionar após o sucesso
    def get_success_url(self):
        return reverse('detalhe_imovel', kwargs={'pk': self.object.pk})