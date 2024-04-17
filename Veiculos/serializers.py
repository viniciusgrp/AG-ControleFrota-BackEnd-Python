from rest_framework import serializers
from .models import Veiculo

class VeiculoSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Veiculo
        fields = ["id", "placa", "marca", "veiculo", "km_troca_oleo"]
        read_only_fields = ["id"]