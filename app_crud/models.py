# Create your models here.
from django.db import models

class Equipamento(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField(blank=True, null=True)
    numero_patrimonio = models.CharField(max_length=50, unique=True)
    data_aquisicao = models.DateField()
    status = models.CharField(
        max_length=20,
        choices=[
            ('disponível', 'Disponível'),
            ('em uso', 'Em uso'),
            ('em manutenção', 'Em manutenção'),
            ('descartado', 'Descartado'),
        ],
        default='disponível'
    )

    def __str__(self):
        return f"{self.nome} - {self.numero_patrimonio}"
