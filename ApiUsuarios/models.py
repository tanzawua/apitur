from enum import auto
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class Servicio(models.Model):
    referencia = models.CharField(max_length=200)
    nombre = models.CharField(max_length=200)
    precio = models.IntegerField()
    nuevo = models.BooleanField()
    descripcion = models.TextField()
    fecha = models.DateField(auto_now_add=True)