from .models import Veiculo
from .serializers import VeiculoSerializer
from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView, RetrieveAPIView, ListAPIView

class CreateVeiculoView(CreateAPIView):
    queryset = Veiculo.objects.all()
    serializer_class = VeiculoSerializer

class VeiculoView(RetrieveUpdateDestroyAPIView):
    queryset = Veiculo.objects.all()
    serializer_class = VeiculoSerializer

    lookup_field = 'id'
    lookup_url_kwarg = 'veiculo_id'

    def perform_update(self, serializer):
        serializer.save()
    
class ListVeiculosView(ListAPIView):
    queryset = Veiculo.objects.all()
    serializer_class = VeiculoSerializer