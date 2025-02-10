from django.db import models

# Create your models here.

class Products(models.Model):
    nome = models.CharField(max_length=255)
    preco = models.FloatField()
    parcelamento = models.TextField()
    imagem = models.URLField()
    link = models.URLField(unique=True)
    preco_original = models.FloatField(null=True, blank=True)
    percentual_desconto = models.FloatField(null=True, blank=True)
    frete_gratis = models.BooleanField(default=False)
    tipo_entrega = models.CharField(max_length=20, choices=[
        ('Normal', 'NORMAL'),
        ('full', 'FULL')
    ])
        
    def __str__(self):
            return f'{self.nome}'

