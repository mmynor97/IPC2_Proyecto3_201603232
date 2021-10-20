from io import IOBase
import xml.etree.ElementTree as ET
from Clases.DTE import DTE
from Clases.Lista import Lista
import re
class File_Xml:
    
    def __init__(self,file):
        self.file = file
        self.correcta = 0
        self.incorrecta = 0
        self.lista_xml = Lista()
        
    def read(self):
        root = None
        print("archivo: "+self.file+"-------------")
        try:
            tree = ET.parse(self.file)
            root = tree.getroot()
        except IndexError:
            print("Error al cargar el archivo")
        print("cargando......")
        if root != None:
            configuracion=self.__parse(root)
        
        return configuracion

    def __parse(self,root):
        for child in root:
            try:
                if "DTE" == child.tag:
                    dte = DTE()
                    for atribute in child:
                        #print(atribute.tag)
                        if "TIEMPO" == atribute.tag:
                            dte.tiempo = atribute.text
                        elif "REFERENCIA" == atribute.tag:
                            dte.referencia = atribute.text
                        elif "NIT_EMISOR" == atribute.tag:
                            dte.nit_emisor = atribute.text
                        elif "NIT_RECEPTOR" == atribute.tag:
                            dte.nit_receptor = atribute.text
                        elif "VALOR" == atribute.tag:
                            dte.valor = atribute.text
                        elif "IVA" == atribute.tag:
                            dte.iva = atribute.text
                        elif "TOTAL" == atribute.tag:
                            dte.total = atribute.text
                    self.lista_xml.push(dte)
                self.correcta += 1
            except:
                self.incorrecta +=1

        return self.lista_xml

    def readAnalizardor(self,fecha):
        root = None
        print("archivo: "+self.file+"-------------")
        try:
            tree = ET.parse(self.file)
            root = tree.getroot()
        except IndexError:
            print("Error al cargar el archivo")
        print("cargando......")
        if root != None:
            configuracion=self.analizarNitxFecha(root,fecha)
        
        return configuracion

    def analizarNitxFecha(self,root,fechaPost):
        patron = "\d{2}/\d{2}/\d{2}"
        
        for child in root:
            try:
                if "DTE" == child.tag:
                    dte = DTE()
                    for atribute in child:
                        #print(atribute.tag)
                        saltar = False
                        if "TIEMPO" == atribute.tag:
                            resultado = re.findall(patron,atribute.text)
                            print(f'fecha post {fechaPost}')
                            print(f'fecha {resultado[0]}')
                            if resultado[0] == fechaPost:
                                saltar=False
                            else:
                                saltar = True
                                continue
                            dte.tiempo = atribute.text
                        elif "REFERENCIA" == atribute.tag:
                            dte.referencia = atribute.text
                            print(f'referencia {atribute.text}')
                        elif "NIT_EMISOR" == atribute.tag:
                            dte.nit_emisor = atribute.text
                        elif "NIT_RECEPTOR" == atribute.tag:
                            dte.nit_receptor = atribute.text
                        elif "VALOR" == atribute.tag:
                            dte.valor = atribute.text
                        elif "IVA" == atribute.tag:
                            dte.iva = atribute.text
                        elif "TOTAL" == atribute.tag:
                            dte.total = atribute.text
                    
                    if not saltar:
                        print("entro")
                        self.lista_xml.push(dte)
                        
                self.correcta += 1
            except:
                self.incorrecta +=1

        return self.lista_xml
           

     

    
