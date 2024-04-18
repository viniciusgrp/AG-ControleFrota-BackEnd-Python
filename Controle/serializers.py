from rest_framework import serializers
from .models import Controle
from Veiculos.serializers import VeiculoSerializer 
from Motoristas.serializers import MotoristaSerializer 

class ControleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Controle
        fields = ["id", "veiculo", "motorista", "data_saida", "hora_saida", "km_saida", "destino", "data_retorno", "hora_retorno", "km_retorno", "km_percorrido"]
        read_only_fields = ["id"]
class ControleDateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Controle
        fields = ["id", "veiculo", "motorista", "data_saida", "hora_saida", "km_saida", "destino", "data_retorno", "hora_retorno", "km_retorno", "km_percorrido"]
        read_only_fields = ["id"]
        depth = 1

        def get_serializer_context(self):
            context = super().get_serializer_context()
            context['data_pesquisa'] = self.request.query_params.get('data_pesquisa')
            return context

class ListControleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Controle
        fields = ["id", "veiculo", "motorista", "data_saida", "hora_saida", "km_saida", "destino", "data_retorno", "hora_retorno", "km_retorno", "km_percorrido"]
        read_only_fields = ["id"]
        depth = 1