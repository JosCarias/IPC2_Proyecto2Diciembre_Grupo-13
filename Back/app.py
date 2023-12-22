from controladoresClientes import menuCliente
from controladoresProducto import menuProductos
from controladoresFactura import menuFacturas


def MenuApp():
    print("\n==========Punto de venta=========="
          +"\n\t1. Clientes"
          +"\n\t2. Productos"      
          +"\n\t3. Facturas"
          +"\n\t4. Salir")

def app():
    MenuApp()
    opcion = int(input ("\nIngrese el número de la acción que desea realizar:\n"))
    while 1<= opcion and opcion <=4:        
        if opcion == 1:
            menuCliente()
        elif opcion == 2:
            menuProductos()
        elif opcion == 3:
            menuFacturas()
        elif opcion == 4:
            print("A salido del punto de venta")
            break  
        MenuApp()    
        opcion = int(input ("\nIngrese el número de la acción que desea realizar:\n"))

if __name__ == "__main__":
    app()