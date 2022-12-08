from django.shortcuts import render
# Create your views here.
from AppCoder.models import Persona
from django.http import HttpResponse
from django.template import Context, Template
from django.template import loader
from django.views.generic import DeleteView

class BorrarPersona(DeleteView):
	model  = Persona
	success_url = 'AppCoder/desafioMVT.html'

def desafio(request):
    personas = Persona.objects.all()
    return render(request,'AppCoder/desafioMVT.html',{"personas":personas})

def saludo(request):
	return HttpResponse('Hola Django - Coder')

def home(self):
	plantilla = loader.get_template('AppCoder/index.html')
	documento = plantilla.render()
	return HttpResponse(documento)

def landing(self):
	plantilla = loader.get_template('AppCoder/landing.html')
	documento = plantilla.render()
	return HttpResponse(documento)

def elements(self):
	plantilla = loader.get_template('AppCoder/elements.html')
	documento = plantilla.render()
	return HttpResponse(documento)

def generic(self):
	plantilla = loader.get_template('AppCoder/generic.html')
	documento = plantilla.render()
	return HttpResponse(documento)







#def desafio(self):
#	plantilla = loader.get_template('desafioMVT.html')
#	documento = plantilla.render()
#	return HttpResponse(documento)

##modelo sin Loader
#def generic(self):
#	miHtml = open('C:/Proyectospython/ProyectoCoder/ProyectoCoder/Plantillas/generic.html')
#	plantilla = Template(miHtml.read())
#	miHtml.close()
#	miContexto = Context()
#	documento = plantilla.render(miContexto)
#	return HttpResponse(documento)