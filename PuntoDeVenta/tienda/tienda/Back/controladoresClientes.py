from cliente import Cliente
from lista_simple import *

lista_clientes = ListaSimple()

def subMenuClientes():
    print("==========Clientes=========="
          +"\n\t1. Agregar clientes"
          +"\n\t2. Editar clientes"      
          +"\n\t3. Eliminar por nombre de cliente"
          +"\n\t4. Ver clientes"
          +"\n\t5. Buscar por nombre cliente"
          +"\n\t6. Salir")

def AgregarCliente():
    dpi = input('Ingrese el DPI del cliente:\n')
    nit = input('Ingrese el NIT del cliente:\n')
    nombre = input('Ingrese el nombre del cliente:\n')
    direccion = input('Ingrese la direccion del cliente:\n')
    correo = input('Ingrese el correo del cliente:\n')
    nuevoCliente = Cliente(dpi,nit,nombre,direccion,correo)
    lista_clientes.insertarNodo(nuevoCliente)

def EditarCliente():
    nombre = input('Ingrese el nombre del cliente a editar\n')
    if lista_clientes.BuscarPorNombre(nombre):
        nuevoNombre = input('Ingrese el nuevo nombre:\n')
        dpi = input('Ingrese el nuevo DPI:\n')
        nit =input('Ingrese el nuevo NIT:\n')
        direccion=input('Ingrese la nueva dirección:\n')
        correo = input('Ingrese el nuevo correo:\n')
        lista_clientes.EditarPorNombreCliente(nombre,dpi,nit,nuevoNombre,direccion,correo)
        print('Editado con éxito')

def EliminarCliente():
    nombre = input('Ingrese el nombre del cliente a eliminar:\n')
    if lista_clientes.BuscarPorNombre(nombre):
        eliminado = lista_clientes.EliminarPorNombre(nombre)
        print('La información del cliente eliminado:\n')
        print('DPI: '+eliminado.dpi)
        print('NIT: '+eliminado.nit)
        print('Nombre: '+eliminado.nombre)
        print('Dirección: '+eliminado.direccion)
        print('Correo: '+eliminado.correo)

def VerClientes():
    lista_clientes.ImprimirCliente()

def BuscarClientePorNombre():
    nombre = input('Ingrese el nombre del cliente que desea buscar:\n')
    busqueda = lista_clientes.BuscarPorNombre(nombre)
    if busqueda:
        print('cliente encontrado:\n')
        print('Nombre: '+busqueda.nombre)
        print('DPI: '+busqueda.dpi)
        print('NIT: '+busqueda.nit)
        print('Dirección: '+busqueda.direccion)
        print('Correo: '+busqueda.correo)
    else:
        print('El nombre del cliente ingresado no existe')

def menuCliente():
    subMenuClientes()
    opcion = int(input ("\nIngrese el número de la acción que desea realizar:\n"))
    while 1<= opcion and opcion <=6:        
        if opcion == 1:
            AgregarCliente()
        elif opcion == 2:
            EditarCliente()
        elif opcion == 3:
            EliminarCliente()
        elif opcion == 4:
            VerClientes()
        elif opcion == 5:
            BuscarClientePorNombre()
        elif opcion == 6:
            print("A salido del sub menú de clientes")
            break  
        subMenuClientes()    
        opcion = int(input ("\nIngrese el número de la acción que desea realizar:\n"))

if __name__ == "__main__":
    menuCliente()
