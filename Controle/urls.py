from django.urls import path
from .views import CreateControleView, UpdateControleView, ListControleView, DateListView

urlpatterns = [
    path("controle/", CreateControleView.as_view()),
    path("controle/date/", DateListView.as_view()),
    path("controle/<int:controle_id>/", UpdateControleView.as_view()),
    path("controle/get/", ListControleView.as_view()),
]
