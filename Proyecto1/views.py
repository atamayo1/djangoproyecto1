from django.http import HttpResponse
from django.template import Template, Context
import datetime
from django.template.loader import get_template
from django.shortcuts import render
#from django.template import loader

class Persona(object):
    def __init__(self, name, lastname):
        self.name = name
        self.lastname = lastname

def hello(request): #primera vista
    #name = "Anthony"
    #lastname = "Tamayo Ortega"

    #doc_extern = open("Proyecto1/templates/template1.html")
    #plt = Template(doc_extern.read())
    #doc_extern.close()
    #doc_extern = get_template('template1.html')
    #ctx = Context({"nombre_persona": p1.name, "apellido_persona": p1.lastname, "fecha_actual": actual_date, "teams":teams})
    #document = doc_extern.render({"nombre_persona": p1.name, "apellido_persona": p1.lastname, "fecha_actual": actual_date, "teams":teams})
    p1 = Persona("Anthony", "Tamayo Ortega")
    teams = ["Plantillas", "Modelos", "Formularios", "Despliegue"]
    actual_date = datetime.datetime.now()

    return render(request, "template1.html", {"nombre_persona": p1.name, "apellido_persona": p1.lastname, "fecha_actual": actual_date, "teams":teams})

def cursodjango(request):
    actual_date = datetime.datetime.now()
    return render(request, "cursodjango.html", {"give_me_date": actual_date})

def bye(request):
    return HttpResponse("Hasta luego alumnos de Django")

def get_date(request):
    actual_date=datetime.datetime.now()
    document="""<html>
        <body>
        <h1>
        Fecha y hora actuales %s
        </h1>
        </body>
        </html>""" % actual_date
    return HttpResponse(document)

