from producto import Producto
from lista_simple import *

lista_productos = ListaSimple()

def subMenuProductos():
    print("==========Productos=========="
          +"\n\t1. Agregar producto"
          +"\n\t2. Editar producto"      
          +"\n\t3. Eliminar por nombre de producto"
          +"\n\t4. Ver productos"
          +"\n\t5. Buscar por nombre producto"
          +"\n\t6. Salir")

def AgregarProducto():
    id = input('Ingrese el Id del producto:\n')
    nombre = input('Ingrese el nombre del producto:\n')
    descripcion = input('Ingrese la descripcion del producto:\n')
    precio = input('Ingrese el precio del producto:\n')
    stock = input('Ingrese el stock del producto:\n')
    nuevoProducto = Producto(id,nombre,descripcion,precio,stock)
    lista_productos.insertarNodo(nuevoProducto)

def EditarProducto():
    nombre = input('Ingrese el nombre del producto a editar\n')
    if lista_productos.BuscarPorNombre(nombre):
        nuevoNombre = input('Ingrese el nuevo nombre:\n')
        id = input('Ingrese el nuevo Id:\n')
        descripcion =input('Ingrese la nueva descripción:\n')
        precio=input('Ingrese el nuevo precio:\n')
        stock = input('Ingrese el nuevo stock:\n')
        lista_productos.EditarPorNombreProducto(nombre,id, nuevoNombre, descripcion, precio, stock)
        print('Editado con éxito')

def EliminarProducto():
    nombre = input('Ingrese el nombre del producto a eliminar:\n')
    if lista_productos.BuscarPorNombre(nombre):
        eliminado = lista_productos.EliminarPorNombre(nombre)
        print('La información del producto eliminado:\n')
        print('Id: '+eliminado.id)
        print('Nombre: '+eliminado.nombre)
        print('Descripción: '+eliminado.descripcion)
        print('Precio: '+eliminado.precio)
        print('Stock: '+eliminado.stock)

def VerProductos():
    lista_productos.ImprimirProducto()

def BuscarProductoPorNombre():
    nombre = input('Ingrese el nombre del producto que desea buscar:\n')
    busqueda = lista_productos.BuscarPorNombre(nombre)
    if busqueda:
        print('Producto encontrado:\n')
        print('Id: '+busqueda.id)
        print('Nombre: '+busqueda.nombre)
        print('Descripción: '+busqueda.descripcion)
        print('Precio: '+busqueda.precio)
        print('Stock: '+busqueda.stock)
    else:
        print('El nombre del producto ingresado no existe')

def menuProductos():
    subMenuProductos()
    opcion = int(input ("\nIngrese el número de la acción que desea realizar:\n"))
    while 1<= opcion and opcion <=6:        
        if opcion == 1:
            AgregarProducto()
        elif opcion == 2:
            EditarProducto()
        elif opcion == 3:
            EliminarProducto()
        elif opcion == 4:
            VerProductos()
        elif opcion == 5:
            BuscarProductoPorNombre()
        elif opcion == 6:
            print("A salido del sub menú de productos")
            break  
        subMenuProductos()    
        opcion = int(input ("\nIngrese el número de la acción que desea realizar:\n"))

if __name__ == "__main__":
    menuProductos()
