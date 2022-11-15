from django.shortcuts import render
# Create your views here.
from AppCoder.models import Persona

def desafio(request):
    personas = Persona.objects.all()
    return render(request,'desafioMVT.html',{"personas":personas})