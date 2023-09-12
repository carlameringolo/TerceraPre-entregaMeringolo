from django.http import HttpResponse
from django.shortcuts import render
from .models import Curso

# Create your views here.


#creo una funcionalidad
def curso(req,nombre,camada):
    curso=Curso(nombre=nombre,camada=camada)
    #despues de generar el objeto de tipo curso, para que impacte en la base de datos tengo que hacer
    curso.save()

    #tengo que retornar algo que le diga al usuario que se guardo correctamente 
    return HttpResponse(f'''<p>Curso: {curso.nombre} - Camada: {curso.camada} creado con exito</p>''')

#recuperar los cursos creados
def listar_cursos(req):
    #le tengo que hacer una consulta a mi base de datos
    #consulta para recuperar informacion (para guardar lo hice arriba)
    #uso el model Curso porque quieor recuperar informacion de la tabla de cursos
    # .objects es para acceder a los manager
    #cuando hago .object me sale el listado de los managers
    #selecciono all que me recupera todo
    lista=Curso.objects.all()
    #aca etsoy diciendo, traeme todos los cursos de la base de datos
    #los guardo en lista
    #le digo renderiza el html que se llama lista_cursos (que cree en la carpeta templates)
    #y pasale como contexto dentro de la key lista_cursos la lista que recuperamos de la base de datos
    return render(req,'lista_cursos.html',{'lista_cursos': lista})


