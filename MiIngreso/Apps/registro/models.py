from django.db import models

# Create your models here.


class Usuario(models.Model):

    ci = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    correo = models.EmailField(max_length=50)
    telefono = models.IntegerField()

