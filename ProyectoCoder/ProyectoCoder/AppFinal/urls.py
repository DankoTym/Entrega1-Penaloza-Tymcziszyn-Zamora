from django.urls import path
from AppFinal import views

urlpatterns = [
    path('', views.Inicio, name="inicio"),
]