from flask import Flask, request
from flask_cors import CORS
from Clases.File_Xml import File_Xml
from Clases.Output import Output
app = Flask(__name__)
CORS(app)


@app.route('/datos', methods=['POST'])
def getDatos():
    cadena=request.json['cadena']
    with open('bdd/entrada.xml', 'w') as archivo:
        archivo.write(cadena)
    archivo.close()

    scanner = File_Xml('bdd/entrada.xml')
    result=scanner.read()
    
    salida=Output(result)
    salida.write(result.correcta,result.incorrecta)

    cadena_salida=None
    with open('bdd/entrada.xml', 'r') as scann:
        for linea in scann:
            cadena_salida +=linea

    return cadena_salida

    


if __name__== '__main__':
    app.run(host='0.0.0.0',debug=True,port=4000)