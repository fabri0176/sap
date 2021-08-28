from django.forms import modelform_factory
from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from personas.forms import PersonaForm
from personas.models import Persona


def detallePersona(request, id):
    # persona = Persona.objects.get(pk=id)
    persona = get_object_or_404(Persona, pk=id)
    return render(request, 'personas/detalle.html', {'persona': persona})


# PersonaForm = modelform_factory(Persona, exclude=[])


def nuevaPersona(request):
    if request.method == 'POST':
        formatPersona = PersonaForm(request.POST)
        if formatPersona.is_valid():
            formatPersona.save()
            return redirect('index')
    else:
        formatPersona = PersonaForm()
    return render(request, 'personas/nueva.html', {'formatPersona': formatPersona})


def editarPersona(request, id):
    persona = get_object_or_404(Persona, pk=id)
    if request.method == 'POST':
        formatPersona = PersonaForm(request.POST, instance=persona)
        if formatPersona.is_valid():
            formatPersona.save()
            return redirect('index')
    else:
        formatPersona = PersonaForm(instance=persona)
    return render(request, 'personas/editar.html', {'formatPersona': formatPersona})


def eliminarPersona(request, id):
    persona = get_object_or_404(Persona, pk=id)
    if persona:
        persona.delete()
    return redirect('index')
