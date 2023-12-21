class Factura:

    def __init__(self, numero, nit, nombre, total, productos = []) -> None:
        self.numero = numero
        self.nit = nit
        self.nombre = nombre
        self.total = total
        self.productos = productos


    def __str__(self) -> str:
        producto = ''
        for product in self.productos:
            producto += str(product)
        return  str(self.numero) + ", " + + str(self.nit) + ", " +  str(self.nombre) + ", " + str(self.total) + ", " + "[ " + producto + "] " 