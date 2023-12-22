from factura import Factura
from lista_simple import *
from controladoresClientes import *
from controladoresProducto import *

lista_facturas = ListaSimple()

def subMenuFacturas():
    print("==========Facturas=========="
          +"\n\t1. Ver nombre de los clientes existentes"
          +"\n\t2. Ver nombre de los productos existenes"      
          +"\n\t3. Agregar factura"
          +"\n\t4. Editar factura"
          +"\n\t5. Eliminar facturas"
          +"\n\t6. Ver facturas"
          +"\n\t7. Agregar producto en factura"
          +"\n\t8. Eliminar producto en factura"
          +"\n\t9. Ver productos en facturas"
          +"\n\t10. Salir")

def VerNombreClientesExistentes():
    nodo = Cliente('dpi1','nit1','cliente1','','correo1')
    lista_clientes.insertarNodo(nodo)
    tamanio=int(lista_clientes.cantidadElementos())
    print('Clientes existentes:\n')
    for i in range(tamanio):
        cliente = lista_clientes.BuscarPorIndice(i)
        print(cliente.nombre)

def VerNombreProductosExistentes():
    nodo = Producto('id1','producto1','empacado','15','20')
    lista_productos.insertarNodo(nodo)
    tamanio = int(lista_productos.cantidadElementos())
    print('Nombre de los productos existentes:\n')
    for i in range(tamanio):
        producto = lista_productos.BuscarPorIndice(i)
        print(producto.nombre)

def AgregarFactura():
    nombreCliente = input('Ingrese el nombre de un clientes existente:\n')
    busqueda = lista_clientes.BuscarPorNombre(nombreCliente)
    if busqueda:
        numeroFactura = input('Ingrese el número de la factura:\n')
        nit = busqueda.nit
        nombre = busqueda.nombre
        total = input('Ingrese el total de la factura:\n')
        nuevaFactura = Factura(numeroFactura,nit,nombre,total)
        lista_facturas.insertarNodo(nuevaFactura)
    else:
        print(f'No existe un cliente llamado: {nombreCliente}')

def EditarFactura():
    nombre = input('Para editar la factura ingrese el nombre del cliente al cual pertenece la factura\n')
    busqueda = lista_facturas.BuscarPorNombre(nombre)
    if busqueda:
        nuevoNombre = input('Ingrese el nuevo nombre:\n')
        busquedaExistenciaCliente = lista_clientes.BuscarPorNombre(nuevoNombre)
        if busquedaExistenciaCliente:
            numeroFactura = input('Ingrese el nuevo número de la factura:\n')
            nit = busqueda.nit
            nombreNuevo = busqueda.nombre
            total = input('Ingrese el nuevo total de la factura:\n')
            lista_facturas.EditarPorNombreFactura(nombre,numeroFactura,nit,nombreNuevo,total)
        else:
            print(f'No existe un cliente llamado: {nuevoNombre}')
        print('Editado con éxito')





def menuFacturas():
    subMenuFacturas()
    opcion = int(input ("\nIngrese el número de la acción que desea realizar:\n"))
    while 1<= opcion and opcion <=10:        
        if opcion == 1:
            VerNombreClientesExistentes()
        elif opcion == 2:
            VerNombreProductosExistentes()
        elif opcion == 3:
            AgregarFactura()
        elif opcion == 4:
            EditarFactura()
        elif opcion == 5:
            pass
        elif opcion == 6:
            pass
        elif opcion == 7:
            pass
        elif opcion == 8:
            pass
        elif opcion == 9:
            pass
        elif opcion == 10:
            print("A salido del sub menú de facturas")
            break  
        subMenuFacturas()    
        opcion = int(input ("\nIngrese el número de la acción que desea realizar:\n"))

if __name__ == "__main__":
    menuFacturas()