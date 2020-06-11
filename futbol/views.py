from django.shortcuts import render
from futbol.models import Jugador
from django.db import IntegrityError

# Create your views here.
def carga(request):

    try:
        if request.method == 'POST':
            nombre = request.POST.get('nombre')
            numero = request.POST.get('numero')
            jugador = Jugador()
            jugador.nombre = nombre
            jugador.numero = numero
            jugador.save()
    except IntegrityError as e:
        if 'unique constraint' in e.message: 
            error = "El jugador ingresado ya existe"
            return render(request, 'futbol.html',{'error':error})
    finally:
        lista = Jugador.objects.all()
        return render(request, 'futbol.html',{'lista':lista})