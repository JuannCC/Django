from http.client import HTTPResponse


from django.http import HttpResponse

def saludo(request):
    return HttpResponse("Hola Mundo")

def despedida(request):
    return HttpResponse("Chau Mundo")

def adulto(request, edad):
    if edad >= 18:
        return HttpResponse("Eres Mayor de edad")
    else:
        return HttpResponse("No eres Mayor de edad")