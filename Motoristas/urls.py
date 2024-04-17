from django.urls import path
from .views import MotoristaView, CreateMotoristaView, ListMotoristasView

urlpatterns = [
    path("motoristas/", CreateMotoristaView.as_view()),
    path("motoristas/<int:motorista_id>/", MotoristaView.as_view()),
    path("motoristas/get/", ListMotoristasView.as_view()),
]
