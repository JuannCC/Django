import email
from django.shortcuts import render
from django.http import HttpResponse
from .models import Author,Entry

def update(request):
    author = Author.objects.get(id=1)
    author.name= "Juan Cruz"
    author.email="juancruzcrotta@gmail.com"
    author.save()
    return HttpResponse("Modificado")

def queries(request):
    # Obtener todos los elementos
    authors = Author.objects.all()

    # Obtener datos filtrados por condicion
    filtred=Author.objects.filter(email="jay25@example.net")

    # Obtener datos filtrados por condicion
    author = Author.objects.get(id=1)

    # Obtener los 10 primeros elementos
    limits = Author.objects.all()[:10]

    # Obtener 5 valores saltenado los 5 primeros
    offset = Author.objects.all()[5:10]

    # Obtener todos los elementos
    orders = Author.objects.all().order_by('email')

    # Obtener todos los elementos cuyo id sea menor a 15
    filters2 = Author.objects.filter(id__lte=15)

    # Obtener todos los autores que contienen en su nombre la palabra yes
    filters3 = Author.objects.filter(name__contains='yes')

    return render(request,"post/queries.html",{'authors':authors, 'filtred':filtred, 'author':author, 'limits':limits, 'offset':offset, 'orders':orders,'filters2':filters2,'filters3':filters3})
