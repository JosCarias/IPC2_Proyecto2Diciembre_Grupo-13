import matplotlib.pyplot as plt
from lista_simple import *
from controladoresClientes import *
from controladoresProducto import *

''' Debe instalar la libreria:
    matplotlib'''

def subMenuReporte():
    print("==========Clientes=========="
          +"\n\t1. Grafica de productos mas vendidos"
          +"\n\t2. Grafica de mejores clientes"
          +"\n\t3. Salir")
    
def GraficaProductosMasVendidos():
    x=[]
    y=[]
    elementos = lista_productos.cantidadElementos()
    if elementos > 0:
        for i in range (elementos):
            numeroVentas=int(lista_productos.BuscarPorIndice(i).cantidadVentas)
            producto=lista_productos.BuscarPorIndice(i).nombre
            if numeroVentas > 0:
                x.append(producto)
                y.append(numeroVentas)
    
    fig,ax = plt.subplots()
    ax.plot(x,y)
    plt.title('Productos más vendidos')
    plt.xlabel('Nombre producto')
    plt.ylabel('Cantidad vendido')
    plt.show()

def menuReporte():
    subMenuReporte()
    opcion = int(input ("\nIngrese el número de la acción que desea realizar:\n"))
    while 1<= opcion and opcion <=3:        
        if opcion == 1:
            GraficaProductosMasVendidos()
        elif opcion == 2:
            pass
        elif opcion == 3:
            print("A salido del sub menú de reportes")
            break  
        subMenuReporte()    
        opcion = int(input ("\nIngrese el número de la acción que desea realizar:\n"))

if __name__ == "__main__":
    menuReporte()