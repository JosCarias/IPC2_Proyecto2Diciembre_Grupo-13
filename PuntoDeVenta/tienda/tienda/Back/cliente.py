class Cliente:

    def __init__(self, dpi, nit, nombre, direccion, correo):
        self.dpi = dpi
        self.nit = nit
        self.nombre = nombre
        self.direccion = direccion
        self.correo = correo

    def __str__(self) -> str:
        return str(self.dpi) + ", " + str(self.nit) + ", " + str(self.nombre) + ', ' + str(self.direccion) + ', ' + str(self.correo)