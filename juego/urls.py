from django.urls import path

from . import views

from juego.views import cargar_habilidad,cargar_personaje,cargar_profesion,modificar_personaje,eliminar_personaje


#urlpatterns = [
    #path('', views.cargar_profesion, name='cargar_profesion'),
#]

urlpatterns = [
    path('juego/cargar_profesion', cargar_profesion),
    path('juego/cargar_habilidad', cargar_habilidad),
    path('cargar_personaje', cargar_personaje),
    path('juego/personaje/<int:id_personaje>', modificar_personaje),
    path('modificar_personaje', modificar_personaje),
    path('juego/', cargar_personaje),
    path('juego/personaje', cargar_personaje),
    path('juego/eliminar/<int:id_personaje>', eliminar_personaje),
]