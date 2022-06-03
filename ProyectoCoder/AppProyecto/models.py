from django.db import models

class Contacto(models.Model):
    nombre = models.CharField(max_length=50)    #nombre completo 
    descripcion = models.CharField(max_length=50)
    email = models.EmailField()

class Producto(models.Model):
    nombre = models.CharField(max_length=20)    #nombre o breve descripcion del producto
    articulo = models.IntegerField()            #número de articulo

class Cliente(models.Model):
    nombre = models.CharField(max_length=50)    #nombre completo 
    email = models.EmailField()
