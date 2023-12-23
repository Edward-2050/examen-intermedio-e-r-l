from django.db import models

# Create your models here.
class Meseros(models.Model):
    nombre = models.CharField(max_length=25)
    nacionalidad = models.CharField(max_length=30)
    edad = models.IntegerField()
    dni = models.CharField(max_length=8, default='00000000')