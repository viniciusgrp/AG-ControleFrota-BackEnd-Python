from django.urls import path
from .views import VeiculoView, CreateVeiculoView, ListVeiculosView

urlpatterns = [
    path("veiculos/", CreateVeiculoView.as_view()),
    path("veiculos/<int:veiculo_id>/", VeiculoView.as_view()),
    path("veiculos/get/", ListVeiculosView.as_view()),
]