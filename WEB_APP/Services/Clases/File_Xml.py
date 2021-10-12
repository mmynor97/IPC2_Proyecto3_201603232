import xml.etree.ElementTree as ET
from Clases.DTE import DTE
from Clases.Lista import Lista
class File_Xml:
    lista_xml = Lista()
    def __init__(self,file):
        self.file = file
        self.correcta = 0
        self.incorrecta = 0

    def read(self):
        root = None
        try:
            tree = ET.parse(self.file)
            root = tree.getroot()
        except:
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
                        if "TIEMPO" == atribute.tag:
                            dte.tiempo = int(atribute.text)
                        elif "REFERENCIA"==atribute.tag:
                            dte.referencia = atribute.text
                        elif "NIT_EMISOR"==atribute.tag:
                            dte.nit_emisor = atribute.text
                        elif "NIT_RECEPTOR"==atribute.tag:
                            dte.nit_receptor = atribute.text
                        elif "VALOR"==atribute.tag:
                            dte.valor = int(atribute.text)
                        elif "IVA" ==atribute.tag:
                            dte.iva = int(atribute.text)
                        elif "TOTAL" == atribute.tag:
                            dte.total = int(atribute.text)
                            
                    self.lista_xml.push(dte)
                self.correcta += 1
            except:
                self.incorrecta +=1

        return self.lista_xml
           

     

    
