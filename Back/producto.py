class Producto:

    def __init__(self, id, nombre, descripcion, precio, stock):
        self.id = id
        self.nombre = nombre
        self.descripcion = descripcion
        self.precio = precio
        self.stock = stock

    
    def __str__(self) -> str:
        return str(self.id) + ", " + str(self.nombre) + ", " + str(self.descripcion) + ', ' + str(self.precio) + ', ' + str(self.stock)