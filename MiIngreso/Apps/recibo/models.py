from django.db import models


# Create your models here.
#from MiIngreso.Apps.empresa.models import Empresa


class Recibo(models.Model):

    fecha = models.DateField()
    hora = models.IntegerField()
    hora_extra = models.IntegerField()
    hora_extra_especial = models.IntegerField()
    hora_dia_descanso = models.IntegerField()
    hora_dia_feriado = models.IntegerField()
    adelanto = models.DecimalField(decimal_places=2, max_digits=9)
    dia_faltado = models.IntegerField()
    empresa = models.ForeignKey('empresa.Empresa', on_delete=models.CASCADE, null=True, blank=False)
    # DESCUENTOS
    aporte_jubilatorio = models.DecimalField(decimal_places=2, max_digits=9, null=True)
    frl = models.DecimalField(decimal_places=2, max_digits=7, null=True)
    seguro_enfermedad = models.DecimalField(decimal_places=2, max_digits=9, null=True)
    



