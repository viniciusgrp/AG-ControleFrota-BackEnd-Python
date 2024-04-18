from .models import Controle
from .serializers import ControleSerializer, ListControleSerializer,ControleDateSerializer
from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView

class CreateControleView(CreateAPIView):
    queryset = Controle.objects.all()
    serializer_class = ControleSerializer

class ListControleView(ListAPIView):
    queryset = Controle.objects.all()
    serializer_class = ListControleSerializer
    
    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.order_by('-data_saida')
    
class DateListView(ListAPIView):
    serializer_class = ControleDateSerializer

    def get_queryset(self):
        queryset = Controle.objects.all()
        data_pesquisa = self.request.query_params.get('data_pesquisa')

        if data_pesquisa:
            filter = queryset.filter(
                data_saida=data_pesquisa
            )

        return filter

class UpdateControleView(RetrieveUpdateDestroyAPIView):
    queryset = Controle.objects.all()
    serializer_class = ControleSerializer

    lookup_field = 'id'
    lookup_url_kwarg = 'controle_id'