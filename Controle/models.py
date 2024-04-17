from django.db import models
from Veiculos.models import Veiculo
from Motoristas.models import Motorista

# Create your models here.
class Controle(models.Model):
    motorista = models.ForeignKey(Motorista, on_delete=models.CASCADE, related_name='controles')
    veiculo = models.ForeignKey(Veiculo, on_delete=models.CASCADE, related_name='controles')
    data_saida = models.DateField()
    hora_saida = models.TimeField()
    km_saida = models.PositiveIntegerField()
    destino = models.CharField(max_length=128)
    data_retorno = models.DateField()
    hora_retorno = models.TimeField()
    km_retorno = models.IntegerField()
    km_percorrido = models.IntegerField()