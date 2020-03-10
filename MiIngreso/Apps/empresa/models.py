from django.db import models

# Create your models here.


class Grupo(models.Model):

    nombre = models.CharField(max_length=50)


class Subgrupo(models.Model):

    nombre = models.CharField(max_length=50)
    grupo = models.ForeignKey(Grupo, null=False, blank=False, on_delete=models.CASCADE)


class Cargo(models.Model):

    nombre= models.CharField(max_length=15)
    sub_grupo= models.OneToOneField(Subgrupo, on_delete=models.CASCADE, null=False, blank=False)


class Empresa(models.Model):

    rut = models.IntegerField(primary_key=True)
    bps = models.IntegerField()
    bse = models.IntegerField()
    grupo = models.OneToOneField(Grupo, on_delete=models.CASCADE, null=False, blank=False)



