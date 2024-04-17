from rest_framework import serializers
from .models import Controle
from Veiculos.serializers import VeiculoSerializer 
from Motoristas.serializers import MotoristaSerializer 

class ControleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Controle
        fields = ["id", "veiculo", "motorista", "data_saida", "hora_saida", "km_saida", "destino", "data_retorno", "hora_retorno", "km_retorno", "km_percorrido"]
        read_only_fields = ["id"]

class ListControleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Controle
        fields = ["id", "veiculo", "motorista", "data_saida", "hora_saida", "km_saida", "destino", "data_retorno", "hora_retorno", "km_retorno", "km_percorrido"]
        read_only_fields = ["id"]
        depth = 1