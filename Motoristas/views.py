from .models import Motorista
from .serializers import MotoristaSerializer
from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView, RetrieveAPIView, ListAPIView

class CreateMotoristaView(CreateAPIView):
    queryset = Motorista.objects.all()
    serializer_class = MotoristaSerializer

class MotoristaView(RetrieveUpdateDestroyAPIView):
    queryset = Motorista.objects.all()
    serializer_class = MotoristaSerializer

    lookup_field = 'id'
    lookup_url_kwarg = 'motorista_id'

    def perform_update(self, serializer):
        serializer.save()
    
class ListMotoristasView(ListAPIView):
    queryset = Motorista.objects.all()
    serializer_class = MotoristaSerializer