from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from personas.models import Persona


def bienvenido(request):
    num_personas = Persona.objects.count()
    # personas = Persona.objects.all()
    personas = Persona.objects.order_by('nombre','apellido')
    return render(request, 'bienvenido.html', {'num_personas': num_personas, 'personas':personas})

def despedida(request):
    return HttpResponse('Despedida desde DJango')

def contacto(request):
    return HttpResponse('Contacto')