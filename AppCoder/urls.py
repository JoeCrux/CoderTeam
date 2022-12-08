from django.urls import path
from .views import desafio,saludo,home,landing,generic,elements,BorrarPersona

urlpatterns = [
    path('', desafio, name='desafio'),
    path('saludo/', saludo, name='saludo'),
    path('home/', home, name='home'),
    path('landing/', landing, name='landing'),
    path('elements/', elements, name='elements'),
    path('generic/', generic, name='generic'),
    path('delete/<pk>', BorrarPersona.as_view(), name='borrar'),
   
]