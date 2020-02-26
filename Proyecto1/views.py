from django.http import HttpResponse

def saludo(request): #primera vista

    document="""<html>
    <body>
    <h1>
    Hola alumnos esta es nuestra primera página con Django
    </h1>
    </body>
    </html>"""

    return HttpResponse(document)

def despedida(request):

    return HttpResponse("Hasta luego alumnos de Django")

def dameFecha(request):

    fecha_actual=datetime.datetime.now()

    document="""<html>
        <body>
        <h1>
        Fecha y hora actuales %s
        </h1>
        </body>
        </html>""" % fecha_actual

    return HttpResponse(document)

