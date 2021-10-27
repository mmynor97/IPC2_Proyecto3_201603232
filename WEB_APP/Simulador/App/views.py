from django.shortcuts import redirect, render
from django.http import  HttpResponse
from . import models
from .forms import UploadFileForm
from django.http import HttpResponseRedirect
import requests
from reportlab.pdfgen import canvas
from django.http import JsonResponse
import json

url = 'http://localhost:4000/'



def index(request):
    data = {}
    if 'Enviar' in request.POST:
        cadena=request.POST['output']
        print("-----------------")
        print(cadena)
        mybody = {
        'cadena': cadena,
        }
        print('\n'+cadena)
        salida=requests.post(url+'/datos',json=mybody)
        return render(request,'App/index.html', {'cadena':cadena,'salida':salida.text})
    elif 'Eliminar' in request.POST:
        eliminar = requests.post(url+'/datosEliminados')
        return render(request,'App/index.html',data)

    return render(request,'App/index.html',data)
    #return HttpResponse('Hola Mundo')



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
    if 'EnviarG' in request.GET:
        consulta = requests.get(url+'/consultaGeneral')
        return render(request,'App/peticiones.html',{'general': consulta.text})

    elif 'reporteG' in request.GET:
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment ; filename=reporte.pdf'

        consulta = requests.get(url+'/consultaGeneral')

        p = canvas.Canvas(response)

        p.drawString(50,800,consulta.text)
        p.showPage()
        p.save()
        
        return response
    
    
        
    return render(request,'App/peticiones.html',data)

def pdfNit(request):
    if 'reporteFec' in request.POST:
        fecha = request.POST['fechaInicialFec']
        mybody = {
        'fecha': fecha,
        }
        print(mybody)
        consulta=requests.post(url+'/consultaNit',json=mybody)
        
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment ; filename=reporteNit.pdf'

        
        p = canvas.Canvas(response)

        p.drawString(50,800,consulta.text)
        p.showPage()
        p.save()
        
        return response
    
    elif 'graficaFec' in request.POST:
        fecha = request.POST['fechaInicialFec']
        mybody = {
        'fecha': fecha,
        }
        labels = []
        data = []
        labels.append(fecha)
        cantidad = requests.post(url+'/graficaNit',json=mybody)
        cant = int(cantidad.text)
        data.append(cant)
        return render(request,'App/peticiones.html',{
            'labels': fecha,
            'data' : cant 
        })
        
   
        
    
def pdfFecha(request):
    if 'reporteRang' in request.POST:
        fecha1 = request.POST['fechaInicialRang']
        fecha2 = request.POST['fechaFinalRang']
        mybody = {
        'fecha1': fecha1,
        'fecha2': fecha2,
        }
        print(mybody)
        consulta=requests.post(url+'/rangoNit',json=mybody)
        
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment ; filename=reporteFecha.pdf'

        
        p = canvas.Canvas(response)

        p.drawString(50,800,consulta.text)
        p.showPage()
        p.save()
        
        return response
    elif 'graficaRang' in request.POST:
        fecha1 = request.POST['fechaInicialRang']
        fecha2 = request.POST['fechaFinalRang']
        mybody = {
        'fecha1': fecha1,
        'fecha2': fecha2,
        }
        labels = []
        data = []
        query = requests.post(url+'/graficaRango',json=mybody)
        dic = json.loads(query.text)

        for key in dic.keys():
            labels.append(key)
        
           
        
        json_labels = json.dumps(labels)
        for item in dic.values():
            data.append(float(item))
        
        

        json_data = json.dumps(data)
        return render(request,'App/graficaRango.html',{
            'labels': json_labels,
            'data' : json_data 
        })
    
    return HttpResponse('Hola Mundo')


##guardar_archivoXML
def handle_uploaded_file(f):
    with open('App/archivosXML/archivo.xml', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)