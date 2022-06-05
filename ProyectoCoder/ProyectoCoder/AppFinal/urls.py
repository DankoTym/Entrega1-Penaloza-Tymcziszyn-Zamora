from django.urls import path
from AppFinal import views

urlpatterns = [
    path('', views.Inicio, name="inicio"),
    path('productosFormulario/', views.productosFormulario, name="productosFormulario"),
    path('clientesFormulario/', views.clientesFormulario, name="clientesFormulario"),
    path('contactoFormulario/', views.contactoFormulario, name="contactoFormulario"),
]
