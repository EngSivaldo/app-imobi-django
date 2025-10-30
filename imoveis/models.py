# imoveis/models.py (Modelo de Dados do Django)

from django.db import models

# ==============================================================================
# CLASSE IMOVEL: Representa um único anúncio (Casa ou Lote)
# ==============================================================================
class Imovel(models.Model):
    
    # Opções para o tipo de imóvel
    TIPO_CHOICES = (
        ('CASA', 'Casa'),
        ('LOTE', 'Lote'),
    )

    # 1. Informações Básicas
    titulo = models.CharField(max_length=200, verbose_name="Título do Anúncio")
    descricao = models.TextField(verbose_name="Descrição Detalhada")
    
    # 2. Dados Financeiros e de Localização
    preco = models.DecimalField(
        max_digits=12, # Ex: 9.999.999.99
        decimal_places=2, 
        verbose_name="Preço (€)"
    )
    endereco = models.CharField(max_length=255, verbose_name="Morada Completa")
    
    # 3. Classificação
    tipo = models.CharField(
        max_length=4, 
        choices=TIPO_CHOICES, 
        default='CASA', 
        verbose_name="Tipo de Imóvel"
    )
    
    # imoveis/models.py (Dentro da classe Imovel)

# ... campos existentes ...
    
    # Adicionar o campo para a imagem:
    imagem_principal = models.ImageField(
        upload_to='fotos/%Y/%m/%d/', # Guarda as imagens numa subpasta baseada na data
        blank=True,                 # O campo não é obrigatório
        null=True,                  # Pode ser nulo no banco de dados
        verbose_name="Imagem Principal"
    )

# ... restante do código ...
    # 4. Status
    esta_a_venda = models.BooleanField(default=True, verbose_name="Disponível para Venda")
    
    # 5. Datas
    data_criacao = models.DateTimeField(auto_now_add=True, verbose_name="Data de Criação")
    
    # Para o futuro: pode adicionar um campo de imagem
    # imagem_principal = models.ImageField(upload_to='fotos/%Y/%m/%d/', blank=True, null=True)

    # Método que define como o objeto será representado (ex: no painel do Admin)
    def __str__(self):
        return f'{self.titulo} ({self.tipo}) - €{self.preco}'

    # Configurações adicionais para o modelo
    class Meta:
        verbose_name = "Imóvel"
        verbose_name_plural = "Imóveis"
        # Ordena os imóveis do mais recente para o mais antigo por padrão
        ordering = ['-data_criacao']
        
        
# ==============================================================================
# CLASSE IMAGEMIMOVEL: Para armazenar fotos secundárias
# ==============================================================================
class ImagemImovel(models.Model):
    # Relação: Uma Imagem pertence a UM Imóvel (Chave Estrangeira)
    imovel = models.ForeignKey(
        Imovel, 
        on_delete=models.CASCADE, # Se o Imóvel for deletado, as fotos também são
        related_name='galeria'    # Nome que usaremos para aceder às fotos a partir do Imóvel (ex: imovel.galeria.all())
    )
    
    imagem = models.ImageField(
        upload_to='galeria/%Y/%m/%d/', # Guarda as imagens da galeria
        verbose_name="Foto Adicional"
    )
    
    descricao = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f"Imagem para {self.imovel.titulo}"

    class Meta:
        verbose_name = "Imagem da Galeria"
        verbose_name_plural = "Imagens da Galeria"