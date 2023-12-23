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
          +"\n\t6. Ver facturas creadas"
          +"\n\t7. Agregar producto en factura"
          +"\n\t8. Eliminar producto en factura"
          +"\n\t9. Ver descripción de factura y productos"
          +"\n\t10. Salir")

def VerNombreClientesExistentes():
    tamanio=int(lista_clientes.cantidadElementos())
    print('Clientes existentes:\n')
    for i in range(tamanio):
        cliente = lista_clientes.BuscarPorIndice(i)
        print(cliente.nombre)

def VerNombreProductosExistentes():
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


def EliminarFactura():
    nombre = input('Para eliminar una factura, ingrese el nombre del cliente a eliminar:\n')
    buesqueda = lista_facturas.BuscarPorNombre(nombre)
    if buesqueda:
        eliminado = lista_facturas.EliminarPorNombre(nombre)
        print('La información de la factura eliminada:\n')
        print('Número Factura: '+eliminado.numero)
        print('NIT: '+eliminado.nit)
        print('Nombre: '+eliminado.nombre)
        print('Total: '+eliminado.total)


def VerFacturas():
    lista_facturas.ImprimirFactura()

def InsertarProductoEnFactura():
    nombre = input('Ingrese el nombre del cliente, para agregar productos a su factura:\n')
    buesqueda = lista_facturas.BuscarPorNombre(nombre)
    if buesqueda:
        nombreProducto = input('Ingrese el nombre del producto a agregar:\n')
        busquedaProducto = lista_productos.BuscarPorNombre(nombreProducto)
        if busquedaProducto:
            lista_facturas.insertarEnFactura(nombre,busquedaProducto)
        else:
            print(f'No existe producto con nombre: {nombreProducto}')
    else:
        print(f'No existe una factura del cliente:{nombre}')

def EliminarUnProductoFactura():
    nombreFactura = input('Ingrese el nombre del cliente, para eliminar un producto en su factura:\n')
    buesquedaFactura = lista_facturas.BuscarPorNombre(nombreFactura)
    if buesquedaFactura:
        nombreProducto = input('Ingrese el nombre del producto que desea eliminar de la factura:\n')
        busquedaProducto = buesquedaFactura.productos.BuscarPorNombre(nombreProducto)
        if busquedaProducto:
            eliminado = lista_facturas.EliminarProductoEnFactura(nombreFactura,nombreProducto)
            print('La información del producto eliminado:\n')
            print('Id: '+eliminado.id)
            print('Nombre: '+eliminado.nombre)
            print('Descripción: '+eliminado.descripcion)
            print('Precio: '+eliminado.precio)
            print('Stock: '+eliminado.stock)
            print('\n')
        else:
            print(f'No existe el producto: {nombreProducto} en la factura: {nombreFactura}')
    else:
        print(f'No existe una factura del cliente:{nombreFactura}')

def EncabezadoFactura():
    print("\n\t==========Punto de Venta=========="
          +"\n\tDirección: Los Almendros 346, Ciudad de Guatemala"
          +"\n\tNit de la empresa: 123456"
          +"\n\tTelefono: 1002-7812"
          +"\n\t=================================")

def VerFacturaConProductos():
    nombreFactura = input('Ingrese el nombre del cliente, para ver los productos que tiene agregados a su factura:\n')
    busqueda = lista_facturas.BuscarPorNombre(nombreFactura)
    if busqueda:
        EncabezadoFactura()
        lista_facturas.ImprimirProductoEnFactura(nombreFactura)
    else:
        print(f'No existe una factura del cliente:{nombreFactura}')

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
            EliminarFactura()
        elif opcion == 6:
            VerFacturas()
        elif opcion == 7:
            InsertarProductoEnFactura()
        elif opcion == 8:
            EliminarUnProductoFactura()
        elif opcion == 9:
            VerFacturaConProductos()
        elif opcion == 10:
            print("A salido del sub menú de facturas")
            break  
        subMenuFacturas()    
        opcion = int(input ("\nIngrese el número de la acción que desea realizar:\n"))

if __name__ == "__main__":
    menuFacturas()