from urllib.robotparser import RequestRate
from django.shortcuts import render

def estaticos(request):
    return render(request, 'estaticos.html', {})