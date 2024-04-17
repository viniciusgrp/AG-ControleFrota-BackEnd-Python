from django.db import models

# Create your models here.
class Veiculo(models.Model):
    placa = models.CharField(max_length=8)
    marca = models.CharField(max_length=64)
    veiculo = models.CharField(max_length=64)
    km_troca_oleo = models.PositiveIntegerField()