from django.urls import path

from . import views

from farmacia.views import cargar,cargarempresa


#urlpatterns = [
    #path('', views.cargar_profesion, name='cargar_profesion'),
#]

urlpatterns = [
    path('farmacia', cargar),
    path('farmacia/carga', cargarempresa),

]