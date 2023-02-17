from django.shortcuts import render

def index(request):
    return render(request, 'index.html', {})

def fotografias(request):
    return render(request, 'fotografias.html', {})
