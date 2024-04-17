from django.db import models

# Create your models here.
class Motorista(models.Model):
    cod_motorista = models.CharField(max_length=16)
    nome = models.CharField(max_length=128)
    telefone = models.CharField(max_length=18)
    cnh = models.CharField(max_length=18)