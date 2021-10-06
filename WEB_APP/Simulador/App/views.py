from django.shortcuts import render
from django.http import  HttpResponse

def index(request):
    data = {}
    return render(request,'App/index.html',data)
    #return HttpResponse('Hola Mundo')
# Create your views here.


def archivos(request):
    data = {}
    return render(request,'App/archivos.html',data)

def ayuda(request):
    data = {}
    return render(request,'App/ayuda.html',data)

def peticiones(request):
    data = {}
    return render(request,'App/peticiones.html',data)