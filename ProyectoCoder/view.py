from django.http import HttpResponse
from django.template import Template, Context

def saludo(request):
	return HttpResponse('Hola Django - Coder')

def inicio(self):
	miHtml = open('C:/Proyectospython/ProyectoCoder/ProyectoCoder/Plantillas/index.html')
	plantilla = Template(miHtml.read())
	miHtml.close()
	miContexto = Context()
	documento = plantilla.render(miContexto)
	return HttpResponse(documento)

def landing(self):
	miHtml = open('C:/Proyectospython/ProyectoCoder/ProyectoCoder/Plantillas/landing.html')
	plantilla = Template(miHtml.read())
	miHtml.close()
	miContexto = Context()
	documento = plantilla.render(miContexto)
	return HttpResponse(documento)


def elements(self):
	miHtml = open('C:/Proyectospython/ProyectoCoder/ProyectoCoder/Plantillas/elements.html')
	plantilla = Template(miHtml.read())
	miHtml.close()
	miContexto = Context()
	documento = plantilla.render(miContexto)
	return HttpResponse(documento)

def generic(self):
	miHtml = open('C:/Proyectospython/ProyectoCoder/ProyectoCoder/Plantillas/generic.html')
	plantilla = Template(miHtml.read())
	miHtml.close()
	miContexto = Context()
	documento = plantilla.render(miContexto)
	return HttpResponse(documento)

def desafio(self):
	miHtml = open('C:/Proyectospython/ProyectoCoder/ProyectoCoder/Plantillas/desafioMVT.html')
	plantilla = Template(miHtml.read())
	miHtml.close()
	miContexto = Context()
	documento = plantilla.render(miContexto)
	return HttpResponse(documento)