from django.contrib import admin
from Apps.empresa.models import Subgrupo
from Apps.empresa.models import Cargo, Empresa
from Apps.empresa.models import Grupo
# Register your models here.

admin.site.register(Grupo)
admin.site.register(Subgrupo)
admin.site.register(Cargo)
admin.site.register(Empresa)
