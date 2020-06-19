# Create your models here.
from django.db import models
from django import forms

# Create your models here.
class Profesion(models.Model):
    nombre = models.CharField(max_length=200)

class Habilidades(models.Model):
    nombre = models.CharField(max_length=200)

    profesion = models.ForeignKey(Profesion, on_delete=models.CASCADE, related_name= 'habilidades')
    nivel_min = models.IntegerField()

class Personaje(models.Model):
    nombre = models.CharField(max_length=200)
    nivel = models.IntegerField()
    clase = models.ForeignKey(Profesion, on_delete=models.CASCADE, related_name='personajes')

class Usuario(models.Model):
    correo = models.CharField(max_length=200,unique=True)
    password = models.CharField(max_length=200)