from django.db import models

# Create your models here.
class Persona(models.Model):
    nombres = models.CharField(max_length=40)
    apellidos = models.CharField(max_length=40)
    edad = models.IntegerField()

    def __str__(self):
        return self.nombres + ' ' + self.apellidos