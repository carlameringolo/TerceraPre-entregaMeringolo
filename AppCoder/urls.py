from django.contrib import admin
from django.urls import path
from AppCoder.views import *

urlpatterns = [
    path('agrega-curso/<nombre>/<camada>/', curso),
    path('lista-cursos/', listar_cursos),
    path('', inicio, name='Inicio'),
    path('cursos/', cursos, name='Cursos'),
    path('profesores/', profesores, name='Profesores'),
    path('estudiantes/', estudiantes, name='Estudiantes'),
    path('entregables/', entregables,name='Entregables'),
    path('curso-formulario/', cursoFormulario,name='CursoFormulario'),
    path('profesor-formulario/', profesorFormulario,name='ProfesorFormulario'),
    path('estudiante-formulario/', estudianteFormulario,name='EstudianteFormulario'),
    path('entregable-formulario/', entregableFormulario,name='EntregableFormulario'),
    path('busqueda-camada/', busquedaCamada,name='BusquedaCamada'),
    path('buscar/', buscar,name='Buscar')
]
