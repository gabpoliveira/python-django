from django.shortcuts import render
from .models import Nota

# Create your views here.

def index(request):
    titulo = "Olá, mundo. Primeiro app django."
    notas = Nota.objects.all()
    context = {
        "titulo": titulo,
        "notas": notas
        }
    return render(request, 'notas/index.html', context)
