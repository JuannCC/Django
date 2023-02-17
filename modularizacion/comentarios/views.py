from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponse
from .models import Comment

def test(request):
    return HttpResponse("Funciona correctamente")

def create(request):
    #comment = Comment(name="Juan", score=5, comment= "Este es un comentario")
    #comment.save()
    #comment = Comment.objects.create(name="Alex")
    return HttpResponse("Funciona correctamente el create")

def delete(request):
    #comment = Comment.objects.get(id=1)
    #comment.delete()
    Comment.objects.filter(id=2).delete()
    return HttpResponse("Ruta para probar los borrados")

