from django.shortcuts import redirect, render
from django.http import  HttpResponse
from . import models
from .forms import UploadFileForm
from django.http import HttpResponseRedirect
def index(request):
    data = {}
    return render(request,'App/index.html',data)
    #return HttpResponse('Hola Mundo')
# Create your views here.


def archivos(request):
    data = {}
    form=None
    if request.method == 'POST':
        # Fetching the form data
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(request.FILES['file'])

            #return HttpResponseRedirect('/success/url/')

            Title = request.POST['title']
        #uploadedFile = request.FILES['uploadedFile']
        
        print(Title)
        
        cadena=""
        with open('App/archivosXML/archivo.xml', 'r') as archivo:
            for linea in archivo :
                cadena+=linea
        
        print(cadena)
        data['cadena']=cadena
        return render(request,'App/index.html',{'cadena':cadena})
    else:
        form= UploadFileForm
        
    data['form']=form

    return render(request,'App/archivos.html',{'form': form})

def ayuda(request):
    data = {}
    return render(request,'App/ayuda.html',data)

def peticiones(request):
    data = {}
    return render(request,'App/peticiones.html',data)

def handle_uploaded_file(f):
    with open('App/archivosXML/archivo.xml', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)