from .nodo import Nodo

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

    def insertarEnFactura(self, nombreFactura, node):
        existeFactura = self.BuscarPorNombre(nombreFactura)
        aux = self.primero
        if existeFactura:
            while aux != None:
                if nombreFactura == aux.node.nombre:
                    aux.node.productos.insertarNodo(node)
                    break
                else:
                    aux = aux.siguiente
    
    def obtenerNodoPorIndice(self, indice):
        contador = 0
        aux = self.primero
        
        while aux is not None:
            if contador == indice:
                return aux.node  # Devuelve el nodo en la posición deseada

            aux = aux.siguiente
            contador += 1
        
        # Si el índice está fuera del rango de la lista, puedes manejarlo devolviendo None o levantando una excepción, por ejemplo.
        return None
    
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


    def ImprimirProductoEnFactura(self, nombreFactura):
        existeFactura = self.BuscarPorNombre(nombreFactura)
        aux = self.primero
        if existeFactura:
            while aux != None:
                if nombreFactura == aux.node.nombre:
                    # Imprime los datos de la factura
                    print(f"\nNúmero factura: {aux.node.numero}")
                    print(f"Nombre del cliente: {aux.node.nombre}")
                    print(f"Nit del cliente: {aux.node.nit}")
                    print(f"Número factura: {aux.node.numero}")
                    print(f"Total: {aux.node.total}")
                    print("\nProductos:\n")
                    # Imprime todos los productos almacenados en la factura
                    aux.node.productos.ImprimirProducto()
                    print("=====================")
                    break
                else:
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

    def ImprimirFactura(self):
        aux = self.primero
        while aux != None:
            print('Número de la factura: '+ aux.node.numero)
            print('Nit del cliente: '+ aux.node.nit)
            print('Nombre del cliente: '+ aux.node.nombre)
            print('Total: '+ aux.node.total)
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
    
    # Solo aplica para clientes
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
    
    def EliminarPorNombre(self, nombre):
        if self.primero == None:
            print("La lista está vacía")
            return None
        if self.primero.node.nombre == nombre:
            aux = self.EliminarPrimero()
            return aux
        aux = self.primero
        previo = None
        while aux != None:
            if aux.node.nombre == nombre:
                if aux == self.ultimo:
                    self.ultimo = previo
                    previo.siguiente = None
                    return aux.node
                previo.siguiente = aux.siguiente
                aux.siguiente = None
                return aux.node
            previo = aux
            aux = aux.siguiente
        print("No existe el nombre")
        return None
    
    def EliminarProductoEnFactura(self, nombreFactura,nombreProducto):
        existeFactura = self.BuscarPorNombre(nombreFactura)
        aux = self.primero
        if existeFactura:
            while aux != None:
                if nombreFactura == aux.node.nombre:
                    nodoProducto = aux.node.productos.EliminarPorNombre(nombreProducto)
                    return nodoProducto # Regresa el nodo de producto
                else:
                    aux = aux.siguiente
    
    # Se utiliza unicamente para los clientes
    def EditarPorNombreCliente(self, nombre,dpi,nit,nuevoNombre,direccion,correo):
        aux = self.primero
        if aux != None:
            while aux != None:
                if aux.node.nombre == nombre:
                    aux.node.nombre = nuevoNombre
                    aux.node.dpi = dpi
                    aux.node.nit = nit
                    aux.node.direccion = direccion
                    aux.node.correo = correo
                    break
                else:
                    aux = aux.siguiente

    # Se utiliza unicamente para los productos
    def EditarPorNombreProducto(self, nombre,id, nuevoNombre, descripcion, precio, stock):
        aux = self.primero
        if aux != None:
            while aux != None:
                if aux.node.nombre == nombre:
                    aux.node.id = id
                    aux.node.nombre = nuevoNombre
                    aux.node.descripcion = descripcion
                    aux.node.precio = precio
                    aux.node.stock = stock
                    break
                else:
                    aux = aux.siguiente

    # Se utiliza unicamente para las facturas
    def EditarPorNombreFactura(self, nombre, numero, nit, nuevoNombre,total):
        aux = self.primero
        if aux != None:
            while aux != None:
                if aux.node.nombre == nombre:
                    aux.node.numero = numero
                    aux.node.nit = nit
                    aux.node.nombre = nuevoNombre
                    aux.node.total = total
                    break
                else:
                    aux = aux.siguiente






    # Se utiliza para insertar un producto de un cliente
    def insertarUnProductoEnFactura(self, nombreCliente, node):
        existeCliente = self.EditarPorNombreCliente(nombreCliente)
        aux = self.primero
        if existeCliente:
            while aux != None:
                if nombreCliente == aux.node.nombre:
                    aux.node.productos.insertarNodo(node)
                    return
                else:
                    aux = aux.siguiente

        

if __name__=='__main__':
    from producto import Producto
    from cliente import Cliente
    
    lista_productos = ListaSimple()
    print(lista_productos.cantidadElementos())
    print(lista_productos.BuscarPorNombre('nombre0'))
    for i in range (3):
        nuevoCliente = Cliente('Dpi'+str(i),'nit'+str(i),'nombre'+str(i),'dir'+str(i),'correo'+str(i))

        lista_productos.insertarNodo(nuevoCliente)


    lista_productos.ImprimirCliente()
    print('Editando cliente:\n')
    nombre = input('Ingrese el nombre del cliente a editar:\n')
    if lista_productos.BuscarPorNombre(nombre):
        nuevoNombre = 'nombre1'
        dpi = '123'
        nit ='n23'
        direccion='direccionPrueba'
        correo = 'correoPrueba'
        lista_productos.EditarPorNombreCliente(nombre,dpi,nit,nuevoNombre,direccion,correo)
    
    lista_productos.ImprimirCliente()
    # print(lista_productos.cantidadElementos())

    # print(lista_productos.BuscarPorIndice(2).nombre)
    # print(lista_productos.BuscarPorNombre('nombre1').direccion)
    # print(lista_productos.BuscarPorNit('nit2').direccion)
    # print(lista_productos.EliminarIndice(2).nombre)
    # print(lista_productos.EliminarPorNombre('nombre0').nombre)
    # print('==========')
    # lista_productos.ImprimirCliente()

