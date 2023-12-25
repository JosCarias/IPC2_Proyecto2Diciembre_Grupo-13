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
        numeroFactura = request.POST.get('numeroFactura')
        nit = request.POST.get('nit')
        nombre = request.POST.get('nombre')
        total = request.POST.get('total')

        nuevaFactura = Factura(numeroFactura, nit, nombre, total)  # Crear una instancia de Factura
        lista_facturas.insertarNodo(nuevaFactura)  # Insertar la factura en la lista de facturas

        return render(request, 'agregarFactura.html')  # Renderizar una página de éxito o redirigir a otra vista

    return render(request, 'agregarFactura.html')  

def listar_facturas(request):
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
    return render(request, 'verFacturas.html', {'productos': productos})

# python manage.py runserver
