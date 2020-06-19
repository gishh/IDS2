from django.shortcuts import render
from farmacia.models import Droga, Empresa
from django.db import IntegrityError

# Create your views here.
def cargar(request):
    error=""
    try:
        if request.method == 'POST':
            nombre = request.POST.get('nombre')
            cantidad = request.POST.get('cantidad')
            empresa = request.POST.get('empresa')
            droga = Droga()
            droga.nombre = nombre
            droga.cantidad = cantidad
            droga.empresa_id = empresa
            droga.save()
    except IntegrityError as e:
            error = "La droga ingresada ya existe"
            return render(request, 'droga.html',{'error':error})
    except Exception as e:   
            error = "Error genérico "+ str(e)
            return render(request, 'droga.html',{'error':error})
    finally:
        lista = Droga.objects.all()
        lista2 = Empresa.objects.all()
        return render(request, 'droga.html',{'lista':lista,'lista2':lista2,'error':error})

def cargarempresa(request):
    error=""
    try:
        if request.method == 'POST':
            nombre = request.POST.get('nombre')
            empresa = Empresa()
            empresa.nombre = nombre
            empresa.save()
    except IntegrityError as e:
            error = "La empresa ingresada ya existe"
            return render(request, 'cargarempresa.html',{'error':error})
    except Exception as e:   
            error = "Error genérico"+ str(e)
            return render(request, 'cargarempresa.html',{'error':error})
    finally:
        lista = Empresa.objects.all()
        return render(request, 'cargarempresa.html',{'lista':lista,'error':error})