import xml.etree.cElementTree as ET
from datetime import date
from Clases.Lista import Lista
class Output:
    def __init__(self,lista):
        self.__root("LISTAAUTORIZACIONES")
        self.lista=lista
        self.__factura= Lista()

    def write(self,correcto,incorrecto):
        autorizacion = ET.SubElement(self.__root,"AUTORIZACION")
        
        fecha = ET.SubElement(autorizacion,"FECHA").text=date.today()
        facturas_recibidad = ET.SubElement(autorizacion,"FACTURAS_RECIBIDAD").text = self.lista.tamanio
        error=ET.SubElement(autorizacion,'ERRORES')

        emisor=self.__nitEmisor()
        nitEmisor = ET.SubElement(error,"NIT_EMISOR").text = emisor
        receptor= self.__nitReceptor()
        nitReceptor = ET.SubElement(error,"NIT_RECEPTOR").text = receptor
        valor = self.__valor()
        iva = ET.SubElement(error,"IVA").text = valor
        total = ET.SubElement(error,"TOTAL").text = valor
        refD = self.__refDubplicada()
        ref_duplicada = ET.SubElement(error,"REFERENCIA_DUPLICADA").text = refD

        factura_incorrecta= int(emisor) + int(receptor) +  int(valor) + int(valor) + int(refD)
        correcta = int(self.lista.tamanio) - factura_incorrecta
        factura_correcta = ET.SubElement(autorizacion,"FACTURA_CORRECTA").text = correcta
        cantidad_emisores = ET.SubElement(autorizacion,"CANTIDAD_EMISORES").text = self.__catEmisore()
        cantidad_receptores = ET.SubElement(autorizacion,"CANTIDAD_RECEPTORES").text = self.__cantReceptores

        listado_autorizacion = ET.SubElement(autorizacion,"LISTADO_AUTORIZACIONES")

        for i in self.__factura.tamanio:
            dte = self.__factura.get(i)
            aprobacion = ET.SubElement(autorizacion,"APROBACION")
            referencia = {"ref":dte.refencia}
            nit_emisor = ET.SubElement(aprobacion,"NIT_EMISOR",attrib=referencia).text = dte.nit_emisor
            cod_aprobacion = ET.SubElement(aprobacion,"CODIGO_APROBACION").text = '000000'+str(i)

        total_aprobacion = ET.SubElement(autorizacion,"TOTAL_APROBACIONES").text = correcta

        tree = ET.ElementTree(self.__root)
        path = "bdd"
        tree.write(path+"/salida.xml")
        pass

    def __nitEmisor(self):
        error=0
        verificador = 10
        for i in int(self.lista.tamanio):
            dte = self.lista.get(i)
            nit_emisor=dte.nit_emisor

            posicion=len(nit_emisor)
            sumatoria=0
            for caracter in nit_emisor:
                aux=posicion*caracter
                sumatoria+=aux
                posicion-=1

            mod = sumatoria % 11

            resta = 11 - mod

            resultado= resta % 11

            if not resultado == verificador:
                error+=1
            else:
                self.__factura.push(dte)
        
        return error
                
    def __nitReceptor(self):
        error=0
        verificador = 10
        for i in int(self.lista.tamanio):
            dte = self.lista.get(i)
            nit_receptor=dte.nit_receptor

            posicion=len(nit_receptor)
            sumatoria=0
            for caracter in nit_receptor:
                aux=posicion*caracter
                sumatoria+=aux
                posicion-=1

            mod = sumatoria % 11

            resta = 11 - mod

            resultado= resta % 11

            if not resultado == verificador:
                error+=1
            else:
                self.__factura.push(dte)
        
        return error

    def __valor(self):
        error=0
        for i in int(self.lista.tamanio):
            dte = self.lista.get(i)
            valor=dte.valor

            if int(valor)<0:
                error +=1
            else:
                self.__factura.push(dte)
        return error

    def __refDubplicada(self):
        error=0
        for i in range(self.lista.tamanio):
            dte1=self.list.get(i)
            for j in range(i+1,self.lista):
                dte2 = self.list.get(j)
                if dte1.referencia == dte2.referencia:
                    self.error += 1
                else:
                    self.__factura.push(dte1)
        return error

    def __catEmisore(self):
        aux = self.lista
        emisores = []
        for i in aux.tamanio:
            dte = aux.get(i)
            emisores.append(dte.nit_emisor)
        
        unico = []
        for x in emisores:
            if not x in unico:
                unico.append(x)

        return len(unico)

    def __cantReceptores(self):
        aux = self.lista
        receptores = []
        for i in aux.tamanio:
            dte = aux.get(i)
            receptores.append(dte.nit_receptor)
        
        unico = []
        for x in receptores:
            if not x in unico:
                unico.append(x)

        return len(unico)

        

            