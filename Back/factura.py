from lista_simple import ListaSimple



class Factura:

    def __init__(self, numero, nit, nombre, total) -> None:
        self.numero = numero
        self.nit = nit
        self.nombre = nombre
        self.total = total
        self.productos = ListaSimple()


    def __str__(self) -> str:
        producto = ''
        for product in self.productos:
            producto += str(product)
        return  str(self.numero) + ", " + + str(self.nit) + ", " +  str(self.nombre) + ", " + str(self.total) + ", " + "[ " + producto + "] " 