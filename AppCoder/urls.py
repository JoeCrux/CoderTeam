from django.urls import path
from .views import desafio,saludo,home,landing,generic,elements

urlpatterns = [
    path('', desafio, name='desafio'),
    path('saludo/', saludo, name='saludo'),
    path('home/', home, name='home'),
    path('landing/', landing, name='landing'),
    path('elements/', elements, name='elements'),
    path('generic/', generic, name='generic'),
   
]