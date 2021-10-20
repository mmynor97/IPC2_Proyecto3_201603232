from datetime import date
from Clases.Lista import Lista
class outAnalizador:
    def __init__(self,lista):
        self.cadena=None
        self.lista=lista
        
    def writeNit(self):
        
        for i in range(self.lista.tamanio):
            dte = self.lista.get(i)
            self.cadena = f" DTE {i}: \n"
            self.cadena += f"\tVALOR = {dte.valor}"
            self.cadena += f"\tIVA = {dte.iva}"
            self.cadena += f"\tTOTAL = {dte.total}"
            self.cadena+="\n\n"

        return self.cadena