from django.shortcuts import render, redirect
from juego.models import Profesion, Habilidades, Personaje, Usuario


def cargar_profesion(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        profesion = Profesion()
        profesion.nombre = nombre
        profesion.save()

    lista = Profesion.objects.all()
    return render(request, 'profesion_carga.html',{'lista':lista})

def cargar_habilidad(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        profesion_id = request.POST.get('profesion')
        nivel = request.POST.get('nivel')
        habilidad = Habilidades()
        habilidad.nombre = nombre
        habilidad.profesion_id = profesion_id
        habilidad.nivel_min = nivel
        habilidad.save()

    lista = Habilidades.objects.all()
    profesiones = Profesion.objects.all()
    return render(request, 'habilidad_carga.html',{'lista':lista,'profesiones':profesiones})

def cargar_personaje(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        profesion_id = request.POST.get('profesion')
        nivel = request.POST.get('nivel')
        personaje = Personaje()
        personaje.nombre = nombre
        personaje.clase_id = profesion_id
        personaje.nivel = nivel
        personaje.save()
    lista = Personaje.objects.all()
    profesiones = Profesion.objects.all()
    return render(request, 'personajes_carga.html',{'lista':lista,'profesiones':profesiones})

def logueo(request):
    if request.method == 'POST':
        correo = request.POST.get('correo')
        password = request.POST.get('password')
        usuario = Usuario()
        usuario = Usuario.objects.get(correo=correo)
        if (usuario.correo == correo):
            if (usuario.password == password):
                return render(request, 'logueo_ok.html')
            else:  
                mensaje= "La password no se reconoce"
                return render(request, 'logueo.html',{'mensaje':mensaje})
        else:
            mensaje= "El usuario no se reconoce"
            return render(request, 'logueo.html',{'mensaje':mensaje})

    return render(request, 'logueo.html')

    
def registro(request):
    if request.method == 'POST':
        correo = request.POST.get('correo')
        password = request.POST.get('password')
        usuario = Usuario()
        usuario.correo = correo
        usuario.password = password
        usuario.save()
        return redirect('/juego/logueo')
    else:
        return render(request, 'registro.html')

def eliminar_personaje(request, id_personaje):
    personaje = Personaje.objects.get(id=id_personaje)
    personaje.delete()
    return redirect('/juego/personaje')
    #return render(request, 'personajes_modificar.html')

def modificar_personaje(request, id_personaje):

    personaje= Personaje.objects.get(id=id_personaje)

    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        profesion_id = request.POST.get('profesion')
        nivel = request.POST.get('nivel')
        personaje.nombre = nombre
        personaje.clase_id = profesion_id
        personaje.nivel = nivel
        personaje.save()
        return redirect('/juego/personaje')
    profesiones = Profesion.objects.all()
    return render(request, 'personajes_modificar.html',{'profesiones':profesiones,'personaje':personaje})