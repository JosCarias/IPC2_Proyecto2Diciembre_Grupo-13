from django.http import HttpResponse
from django.shortcuts import render
from tienda.Back.cliente import *
from tienda.Back.producto import *
from tienda.Back.factura import *
from tienda.Back.lista_simple import *

lista_clientes = ListaSimple()
lista_productos = ListaSimple()
lista_facturas = ListaSimple()


def hello_world(request):
    return HttpResponse("<h1>Hello world</h1>")

def test_page_view(request):
    return render(request, 'test_page.html')

def index(request):
    return render(request, 'index.html')

def estadisca(request):
    return render(request, 'verGraficas.html')

def agregarCliente(request):
    if request.method == 'POST':
        dpi = request.POST.get('dpi')
        nit = request.POST.get('nit')
        nombre = request.POST.get('nombre')
        direccion = request.POST.get('direccion')
        correo = request.POST.get('correo')

        nuevoCliente = Cliente(dpi,nit,nombre,direccion,correo)  # Crea una instancia de Cliente
        lista_clientes.insertarNodo(nuevoCliente)  # Inserta el cliente en la lista
        print(nuevoCliente.nombre)

        return render(request, 'agregarCliente.html')  # Renderiza una página de éxito o redirige a otra vista

    return render(request, 'agregarCliente.html')    # Ejemplo de respuesta después de agregar el cliente

def listar_clientes(request):
    clientes = []

    # Suponiendo que `lista_clientes` es tu lista enlazada de clientes
    longitud = int(lista_clientes.cantidadElementos())

    # Iterar a través de la lista enlazada para obtener los clientes
    for i in range(longitud):
        cliente = lista_clientes.obtenerNodoPorIndice(i)
        # Asegúrate de agregar solo los atributos necesarios del cliente a la lista
        clientes.append({
            'dpi': cliente.dpi,
            'nit': cliente.nit,
            'nombre': cliente.nombre,
            'direccion': cliente.direccion,
            'correo': cliente.correo
        })

    # Renderizar la plantilla con la lista de clientes
    return render(request, 'verClientes.html', {'clientes': clientes})

def eliminar_cliente(request):
    if request.method == 'GET':
        nombre = request.GET.get('nombre')
        lista_clientes.EliminarPorNombre(nombre) # Eliminar el cliente de la lista

        return render(request, 'eliminarCliente.html')  # Renderiza una página de éxito o redirige a otra vista


def agregar_producto(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        nombre = request.POST.get('nombre')
        descripcion = request.POST.get('descripcion')
        precio = request.POST.get('precio')
        stock = request.POST.get('stock')

        nuevoProducto = Producto(id, nombre, descripcion,precio, stock)  # Crear una instancia de Producto
        lista_productos.insertarNodo(nuevoProducto)  # Insertar el producto en la lista de productos

        return render(request, 'agregarProducto.html')  # Renderizar una página de éxito o redirigir a otra vista

    return render(request, 'agregarProducto.html')

def listar_productos(request):
    productos = []

    # Obtén la longitud de la lista de productos
    longitud = lista_productos.cantidadElementos()

    # Iterar a través de la lista enlazada para obtener los productos
    for i in range(longitud):
        producto = lista_productos.obtenerNodoPorIndice(i)
        print(producto.nombre)

        # Asegúrate de acceder correctamente a los atributos del producto
        productos.append({
            'id': producto.id,
            'nombre': producto.nombre,
            'descripcion': producto.descripcion,
            'precio': producto.precio,
            'stock': producto.stock,
        })
    return render(request, 'verProductos.html', {'productos': productos})

def agregar_factura(request):
    if request.method == 'POST':
        numero = request.POST.get('numeroFactura')
        nombre = request.POST.get('nombreCliente')  # Ajustar el nombre del campo según el formulario
        total = request.POST.get('total')
        nombreProducto = request.POST.get('productos')
        allProducto = nombreProducto.split(',')

        # Este segmento de codigo, sirve para la informacion de la factura
        nit = lista_clientes.BuscarPorNombre(nombre).nit
        nombre = lista_clientes.BuscarPorNombre(nombre).nombre
        total = total
        nuevaFactura = Factura(numero,nit,nombre,total)
        lista_facturas.insertarNodo(nuevaFactura)

        buesqueda = lista_facturas.BuscarPorNombre(nombre)
        if buesqueda:
        # se realiza el ingreso de productos
            for unProducto in allProducto:
                busquedaProducto = lista_productos.BuscarPorNombre(unProducto)
                if busquedaProducto:
                    busquedaProducto.cantidadVentas += 1
                    lista_facturas.insertarEnFactura(nombre,busquedaProducto)

        return render(request, 'agregarFactura.html')  # Página de éxito o redirección

    return render(request, 'agregarFactura.html') 

def listar_facturas(request):
    facturas = []

    # Verificar si existen facturas en la lista antes de iterar
    if lista_facturas.cantidadElementos() > 0:
        longitud = lista_facturas.cantidadElementos()
        if lista_productos.cantidadElementos() > 0:
            tamanio = lista_productos.cantidadElementos()
        # Iterar a través de la lista enlazada para obtener las facturas
            for i in range(longitud):
                productos = []
                for j in range(tamanio):
                    factura = lista_facturas.obtenerNodoPorIndice(i)

                    producto = lista_facturas.obtenerNodoPorIndice(i).productos.obtenerNodoPorIndice(j).nombre
                    productos.append(producto)
                    # Acceder a los atributos correctos de la factura y agregarlos a la lista
                facturas.append({
                    'numeroFactura': factura.numero,  # Acceder al atributo 'numero' en lugar de 'numeroFactura'
                    'nit': factura.nit,
                    'nombre': factura.nombre,
                    'total': factura.total,
                    'productos':productos,
                })

    return render(request, 'verFacturas.html', {'facturas': facturas})

def buscar_Factura(request):
    if request.method == 'POST':
        factura_id = request.POST.get('id')  # Obtén el ID de la factura del formulario
        factura = lista_facturas.buscarPorNumeroFactura(factura_id)     
        productos = []

        # Verificar si la factura se encontró
        if factura:
            # Recuperar los productos asociados a la factura encontrada
            for i in range(factura.productos.cantidadElementos()):
                producto = factura.productos.obtenerNodoPorIndice(i).nombre
                productos.append(producto)

            return render(request, 'buscarFactura.html', {'factura': factura, 'productos': productos})
        else:
            # Si la factura no se encuentra, puedes manejarlo aquí
            mensaje_error = f"No se encontró ninguna factura con el ID: {factura_id}"
            return render(request, 'buscarFactura.html', {'error_message': mensaje_error})

    return render(request, 'buscarFactura.html')


# python manage.py runserver
