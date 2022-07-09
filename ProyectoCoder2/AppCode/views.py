from django.http import HttpResponse
from django.shortcuts import render
from AppCode.models import Curso
# Create your views here.

def curso(self):

    curso= Curso(nombre="pp", comision=9874)
    curso.save()
    texto=f"curso: {curso.nombre}"
    return HttpResponse(texto)