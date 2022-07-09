from django.http import HttpResponse
import datetime
from django.template import Context, Template, loader


def saludar(request):
    return HttpResponse("Hello Kitty!")

def segunda_vista(request):
    return HttpResponse("Ya enendi")

def comer(request):
    return HttpResponse("I'm hungryyyyyy")

def dia_de_hoy(request):
    dia=datetime.datetime.today()
    code="Hoy es: " + str(dia)
    return HttpResponse(code)

def saludo_con_nombre(request, nombre):
    return HttpResponse ("Hola mi nombre es: " +nombre)

def nacimiento(request, edad):
    return HttpResponse ("Tu fecha de nacimiento es: "+str(int(datetime.datetime.now().year)-int(edad)))

def probandoHtml(self):
    
    nom="Feru"
    ape="Kishimoto"
    lista_de_notas=[9,8,7,5,4,3,2,1]

    plantilla=loader.get_template('template2.html')

    diccionario={'nombre':nom, 'apellido':ape, 'lista':lista_de_notas}

    documento=plantilla.render(diccionario)

    return HttpResponse(documento)




