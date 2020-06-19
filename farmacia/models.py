from django.db import models
from django import forms

# Create your models here.

class Empresa(models.Model):
    nombre = models.CharField(max_length=100,unique=True)

class Droga(models.Model):
    nombre = models.CharField(max_length=100,unique=True)
    cantidad = models.IntegerField(unique=True)
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE, related_name='drogas')

    class Meta:
        unique_together = ("nombre", "cantidad")


