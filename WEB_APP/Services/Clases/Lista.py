class Lista:
    def __init__(self):
        self.tamanio = 0
        self.inicio = None
        self.final = None

    def push(self,DTE):
        if self.final == None:
            self.final= DTE
            self.inicio=self.final
            self.tamanio+=1
            
            return True
            
        else:
            temporal = DTE
            self.final.setNext(temporal)
            self.final=temporal
            self.tamanio+=1
            
            return True
        return False

    def pop(self):
        if self.inicio == None:
                print("\nadvertencia: No hay ordenes.\n")
        else:
            temporal = self.inicio
            self.inicio= self.inicio.getNext()
            self.tamanio-=1
        return temporal

    def to_list(self):
        if self.inicio == None:
            print("\nNo hay ordenes\n")           
        else:
            aux = self.inicio
            print("Las Ordenes son: \n")
            while aux != None:
                print(f" nombre: {aux.getOrden().getNombre()} Ingrediente: {aux.getOrden().getIngrediente()}")
                aux = aux.getNext()
            print(" ")

    def get(self,_key):
        temporalNodo = self.inicio
        if temporalNodo!=None:
            for i in range(0, _key, 1):
                temporalNodo = temporalNodo.getNext()
            if temporalNodo != None:
                return temporalNodo
            else:
                return None
        else:
            return None
        pass