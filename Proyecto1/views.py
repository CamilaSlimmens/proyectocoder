from django.http import HttpResponse
from django.template.loader import render_to_string

def saludo(request, nombre):
    body = render_to_string('saludo.html', {'nombre': nombre})
    return HttpResponse(body)