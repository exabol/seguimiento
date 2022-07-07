from django.contrib import admin
from .models import Actividades, Coordinaciones, Funcionarios, Ilcs, Departamentos, ObjetivosEstrategicos, Provincias
# Register your models here.
admin.site.register(Ilcs)
admin.site.register(Departamentos)
admin.site.register(Provincias)
admin.site.register(Coordinaciones)
admin.site.register(ObjetivosEstrategicos)
admin.site.register(Actividades)
admin.site.register(Funcionarios)

 
