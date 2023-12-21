from nodo import Nodo

class ListaSimple:

    def __init__(self):
        self.primero = None
        self.ultimo = None

    def insertarNodo(self, node):
        nuevoNodo = Nodo(node)
        if self.primero is None:
            self.primero = self.ultimo = nuevoNodo
        else: 
            self.ultimo.siguiente = nuevoNodo
            self.ultimo = nuevoNodo

    def ImprimirProducto(self):
        aux = self.primero
        while aux != None:
            print('Id: '+ aux.node.id)
            print('Nombre: '+ aux.node.nombre)
            print('Descripción: '+ aux.node.descripcion)
            print('Precio: '+ aux.node.precio)
            print('Stock: '+ aux.node.stock)
            print('\n')
            aux = aux.siguiente

    def ImprimirCliente(self):
        aux = self.primero
        while aux != None:
            print('DPI: '+ aux.node.dpi)
            print('Nit: '+ aux.node.nit)
            print('Nombre: '+ aux.node.nombre)
            print('Dirección: '+ aux.node.direccion)
            print('Correo: '+ aux.node.correo)
            print('\n')
            aux = aux.siguiente

    def cantidadElementos(self):
        contador = 0
        aux = self.primero
        if aux != None:
            while aux != None:
                contador = contador + 1
                aux = aux.siguiente
            return contador
        else:
            return contador
        
    def BuscarPorIndice(self, indice):
        contador = 0
        aux = self.primero
        while aux and contador != indice:
            aux = aux.siguiente
            contador += 1
        return aux.node
    
    def BuscarPorNombre(self, nombre):
        aux = self.primero
        if aux != None:
            while aux != None:
                if aux.node.nombre == nombre:
                    return aux.node
                else:
                    aux = aux.siguiente

    def BuscarPorNit(self, nit):
        aux = self.primero
        if aux != None:
            while aux != None:
                if aux.node.nit == nit:
                    return aux.node
                else:
                    aux = aux.siguiente
    
    def EliminarPrimero(self):
        if self.primero != None:
            if self.primero.siguiente == None:
                aux = self.primero
                self.primero = None
                self.ultimo = None
                return aux.node
            else:
                aux = self.primero
                self.primero = self.primero.siguiente
                aux.siguiente = None
                return aux.node
    
    def EliminarIndice(self, indice):
        if self.primero == None:
            print("La lista está vacía")
            return None
        if indice == 0:
            aux = self.EliminarPrimero()
            return aux
        if indice < 0:
            print("No existen posiciones menores que cero")
            return None
        aux = self.primero
        contador = 0
        previo = None
        while aux != None:
            if contador == indice:
                if aux == self.ultimo:
                    self.ultimo = previo
                    previo.siguiente = None
                    return aux.node
                previo.siguiente = aux.siguiente
                aux.siguiente= None
                return aux.node
            previo = aux
            aux = aux.siguiente
            contador += 1
        print("No existe la posición indicada")
        return None
        

# if __name__=='__main__':
    # from producto import Producto
    # from cliente import Cliente
    
    # lista_productos = ListaSimple()
    # print(lista_productos.cantidadElementos())
    # for i in range (3):
    #     nuevoCliente = Cliente('Dpi'+str(i),'nit'+str(i),'nombre'+str(i),'dir'+str(i),'correo'+str(i))

    #     lista_productos.insertarNodo(nuevoCliente)


    # lista_productos.ImprimirCliente()
    # print(lista_productos.cantidadElementos())

    # print(lista_productos.BuscarPorIndice(2).nombre)
    # print(lista_productos.BuscarPorNombre('nombre2').direccion)
    # print(lista_productos.BuscarPorNit('nit2').direccion)
    # print(lista_productos.EliminarIndice(2).nombre)
    # print('==========')
    # lista_productos.ImprimirCliente()

