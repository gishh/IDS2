from django.contrib import admin
from django.urls import include, path
import futbol
from futbol.views import carga

urlpatterns = [
    path('fulbito/', carga),
]