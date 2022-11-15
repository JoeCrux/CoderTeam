from django.db import models

# Create your models here.
class Persona(models.Model):
    nombre = models.CharField(max_length=40)
    edad = models.IntegerField()
    fechnac = models.DateField()

    