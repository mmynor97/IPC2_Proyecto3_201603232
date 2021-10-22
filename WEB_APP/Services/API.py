from flask import Flask, jsonify, request, Response
from flask_cors import CORS
from Clases.File_Xml import File_Xml
from Clases.Output import Output
from Clases.outAnalizador import outAnalizador
app = Flask(__name__)
CORS(app)


@app.route('/datos', methods=['POST'])
def getDatos():
    cadena=request.json['cadena']
    with open('bdd/entrada.xml', 'w') as archivo:
        archivo.write(cadena)
    archivo.close()
    print(cadena)
    scanner = File_Xml('bdd/entrada.xml')
    result=scanner.read()
    
    salida=Output(result)
    salida.write()
    
    cadena_salida=None
    with open('bdd/salida.xml', 'r') as scann:
        for linea in scann:
            cadena_salida = linea

    return cadena_salida

@app.route('/datosEliminados', methods=['POST'])
def eliminacion_datos():
    with open('bdd/entrada.xml', 'w') as archivo_entrada:
        archivo_entrada.write("")
    archivo_entrada.close()
    with open('bdd/salida.xml', 'w') as archivo_salida:
        archivo_salida.write("")
    archivo_salida.close()
    pass

@app.route('/consultaGeneral',methods=['GET'])
def consultaG():
    cadena_salida=None
    with open('bdd/salida.xml', 'r') as scann:
        for linea in scann:
            cadena_salida = linea
    
    if cadena_salida == None:
        cadena_salida="No existe base de datos"

    return cadena_salida

@app.route('/consultaNit',methods=['POST'])
def consultaFecNit():

    fecha=request.json['fecha']

    scanner = File_Xml('bdd/entrada.xml')
    result=scanner.readAnalizardor(fecha)
    print(result.tamanio)
        
    salida=outAnalizador(result)
    cadena=salida.writeNit()

    return cadena

@app.route('/graficaNit',methods=['POST'])
def graficaFecNit():

    fecha=request.json['fecha']

    scanner = File_Xml('bdd/entrada.xml')
    result=scanner.readAnalizardor(fecha)
    

    return result.tamanio

@app.route('/rangoNit',methods=['POST'])
def rangoNit():
    fecha1=request.json['fecha1']
    fecha2=request.json['fecha2']

    
    scanner = File_Xml('bdd/entrada.xml')
    result=scanner.readAnalizardorFechaRango(fecha1,fecha2)

    #print(result.tamanio)

    salida=outAnalizador(result)

    cadena=salida.writeNit()

    return cadena
    
    

if __name__== '__main__':
    app.run(host='0.0.0.0', debug=True, port=4000)