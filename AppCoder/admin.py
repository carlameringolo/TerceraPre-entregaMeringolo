from django.contrib import admin
from .models import Curso, Estudiante, Entregables, Profesor

# Register your models here.

admin.site.register(Curso)
admin.site.register(Estudiante)
admin.site.register(Entregables)
admin.site.register(Profesor)
