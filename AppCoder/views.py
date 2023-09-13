from django.http import HttpResponse
from django.shortcuts import render
from .models import Curso, Profesor, Estudiante, Entregables

# Create your views here.

def curso(req,nombre,camada):
    curso=Curso(nombre=nombre,camada=camada)
    curso.save()
    return HttpResponse(f'''<p>Curso: {curso.nombre} - Camada: {curso.camada} creado con exito</p>''')

def listar_cursos(req):

    lista=Curso.objects.all()
  
    return render(req,'lista_cursos.html',{'lista_cursos': lista})



def inicio(req):
    return render(req,'inicio.html')

def cursos(req):
    return render(req,'cursos.html')

def profesores(req):
    return render(req,'profesores.html')

def estudiantes(req):
    return render(req,'estudiantes.html')

def entregables(req):
    return render(req,'entregables.html')



def cursoFormulario(req):
    
    print('method',req.method)
    

    if req.method == 'POST':
        curso=Curso(nombre=req.POST['curso'],camada=req.POST['camada'])
        curso.save()
        return render(req, 'Inicio.html')
    else:
        return render(req, 'cursoFormulario.html')



def profesorFormulario(req):
    if req.method == 'POST':
        profesor=Profesor(nombre=req.POST['nombre'],apellido=req.POST['apellido'],email=req.POST['email'],profesion=req.POST['profesion'])
        profesor.save()
        return render(req, 'Inicio.html')
    else:
        return render(req, 'profesorFormulario.html')


def estudianteFormulario(req):
    if req.method == 'POST':
        estudiante=Estudiante(nombre=req.POST['nombre'],apellido=req.POST['apellido'],email=req.POST['email'])
        estudiante.save()
        return render(req, 'Inicio.html')
    else:
        return render(req, 'estudianteFormulario.html')


def entregableFormulario(req):
    if req.method == 'POST':
        entregable=Entregables(nombre=req.POST['nombre'],fecha=req.POST['fecha'])
        entregable.save()
        return render(req, 'Inicio.html')
    else:
        return render(req, 'entregableFormulario.html')


