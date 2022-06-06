from django.urls import path
from AppFinal import views

urlpatterns = [
    path('', views.Inicio, name="inicio"),
    #Formularios de Carga
    path('productosFormulario/', views.productosFormulario, name="productosFormulario"),
    path('clientesFormulario/', views.clientesFormulario, name="clientesFormulario"),
    path('contactoFormulario/', views.contactoFormulario, name="contactoFormulario"),
    #Formularios de Busqueda
    path('busquedaProductos/', views.busquedaProductos, name="busquedaProductos"),
    path('busquedaClientes/', views.busquedaClientes, name="busquedaClientes"),


    #Buscadores
    path('buscarProducto/', views.buscarProducto, name="buscarProducto"),
    path('buscarClientes/', views.buscarClientes, name="buscarClientes"),
]
