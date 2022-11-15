from django.http import HttpResponse
from django.template import Context, Template
from django.template import loader


def saludo(request):
	return HttpResponse('Hola Django - Coder')

def inicio(self):
	plantilla = loader.get_template('index.html')
	documento = plantilla.render()
	return HttpResponse(documento)

def landing(self):
	plantilla = loader.get_template('landing.html')
	documento = plantilla.render()
	return HttpResponse(documento)

def elements(self):
	plantilla = loader.get_template('elements.html')
	documento = plantilla.render()
	return HttpResponse(documento)

def generic(self):
	plantilla = loader.get_template('generic.html')
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