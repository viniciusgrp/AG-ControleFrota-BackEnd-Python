from rest_framework import serializers
from .models import Motorista

class MotoristaSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Motorista
        fields = ["id", "cod_motorista", "nome", "telefone", "cnh"]
        read_only_fields = ["id"]