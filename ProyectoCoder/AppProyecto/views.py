from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

# Create your views here.

def Inicio(self):
    plantilla = loader.get_template('AppProyecto/inicio.html')   #es importante que la pagina de inicio, tenga un loader.
    documento = plantilla.render()
    return HttpResponse(documento)

"""
def productosFormulario(request):
    if request.method == 'POST':
        miFormulario = ProfesorFormulario(request.POST)
        if miFormulario.is_valid():
            informacion=miFormulario.cleaned_data
        nombre = informacion['nombre']
        apellido = informacion['apellido']
        email = informacion['email']
        profecion = informacion['profecion']

        profesor = Profesor(nombre=nombre, apellido=apellido, email=email, profecion=profecion)
        profesor.save()
        return render(request, "AppCoder/inicio.html")
    else:
        miFormulario = ProfesorFormulario()

    return render(request, 'AppCoder/profesorFormulario.html', {'miFormulario':miFormulario})
"""