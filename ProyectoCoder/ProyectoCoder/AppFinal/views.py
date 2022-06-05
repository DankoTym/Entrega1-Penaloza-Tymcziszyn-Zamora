from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from AppFinal.models import Producto, Cliente, Contacto
from AppFinal.forms import ProductosFormulario, ClienteFormulario, ContactoFormulario

# Create your views here.

def Inicio(self):
    plantilla = loader.get_template('AppFinal/inicio.html')   #es importante que la pagina de inicio, tenga un loader.
    documento = plantilla.render()
    return HttpResponse(documento)


#Carga de datos.
def productosFormulario(request):
    if request.method == 'POST':
        miFormulario = ProductosFormulario(request.POST)
        if miFormulario.is_valid():
            informacion=miFormulario.cleaned_data
        nombre = informacion['nombre']
        articulo = informacion['articulo']

        producto = Producto(nombre=nombre, articulo=articulo)
        producto.save()
        return render(request, "AppFinal/inicio.html")
    else:
        miFormulario = ProductosFormulario()

    return render(request, 'AppFinal/productosFormulario.html', {'miFormulario':miFormulario})

def clientesFormulario(request):
    if request.method == 'POST':
        miFormulario = ClienteFormulario(request.POST)
        if miFormulario.is_valid():
            informacion=miFormulario.cleaned_data
        nombre = informacion['nombre']
        apellido = informacion['apellido']
        email = informacion['email']

        cliente = Cliente(nombre=nombre, apellido=apellido, email=email)
        cliente.save()
        return render(request, "AppFinal/inicio.html")
    else:
        miFormulario = ClienteFormulario()

    return render(request, 'AppFinal/clienteFormulario.html', {'miFormulario':miFormulario})


def contactoFormulario(request):
    if request.method == 'POST':
        miFormulario = ContactoFormulario(request.POST)
        if miFormulario.is_valid():
            informacion=miFormulario.cleaned_data
        nombre = informacion['nombre']
        apellido = informacion['apellido']
        email = informacion['email']

        contacto = Contacto(nombre=nombre, apellido=apellido, email=email)
        contacto.save()
        return render(request, "AppFinal/inicio.html")
    else:
        miFormulario = ContactoFormulario()

    return render(request, 'AppFinal/contactoFormulario.html', {'miFormulario':miFormulario})



"""
def busquedaCamada(request):        #Esta buncion solo recibe el numero de camada que quiero buscar

    return render(request, "AppFinal/busquedaCamada.html")

def buscar(request):               #Esta es la funcion que busca la camada

    #respuesta = f"Estoy buscando la camada nro: {request.GET['camada']}"
    if request.GET['camada']:
        camada =request.GET['camada']               #Hace que camada sea igual a lo que me mandan desde la vista.
        cursos = Curso.objects.filter(camada=camada)    #Realisa una comparacion entre lo que busco y lo que hay cargado.
        return render(request, "AppCoder/resultadosBusqueda.html", {'cursos':cursos, 'camada':camada})
    else:
        respuesta = "No se ingreso ninguna comisión" 
        return HttpResponse(respuesta)
"""