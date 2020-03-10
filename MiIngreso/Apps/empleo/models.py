from django.db import models

# Create your models here.
#from MiIngreso.Apps.empresa.models import Empresa
#from MiIngreso.Apps.registro.models import Usuario


class Empleo(models.Model):

    contrato = models.IntegerField()
    sector = models.CharField(max_length=40)
    cargo = models.CharField(max_length=40)
    fecha_ingreso = models.DateField()
    salario_nominal = models.IntegerField()
    valor_hora = models.DecimalField(decimal_places=2, max_digits=5)
    empresa = models.OneToOneField('empresa.Empresa', on_delete=models.CASCADE, null=True, blank=False)
    usuario = models.OneToOneField('registro.Usuario', on_delete=models.CASCADE, null=True, blank=False)
