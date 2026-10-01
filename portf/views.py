from django.shortcuts import render, redirect, get_object_or_404
from .models import RegistroPrueba
from .forms import RegistroPruebaForm

def inicio(request):
    return render(request, 'data/inicio.html')

def metas(request):
    return render(request, 'data/metas.html')

def lugares(request):
    return render(request, 'data/lugares_maravillosos.html')