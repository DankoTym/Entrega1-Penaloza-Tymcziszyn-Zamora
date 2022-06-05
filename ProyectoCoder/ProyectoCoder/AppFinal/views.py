from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.

def Inicio(self):
    plantilla = loader.get_template('AppFinal/inicio.html')   #es importante que la pagina de inicio, tenga un loader.
    documento = plantilla.render()
    return HttpResponse(documento)