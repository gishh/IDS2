from django.db import models

# Create your models here.
class Jugador(models.Model):
    nombre = models.CharField(max_length=200)
    numero = models.IntegerField(unique=True)