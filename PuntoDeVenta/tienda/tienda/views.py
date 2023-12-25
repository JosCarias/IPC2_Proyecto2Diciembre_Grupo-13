from django.http import HttpResponse
from django.shortcuts import render
from tienda.Back.cliente import *
from tienda.Back.lista_simple import *

lista_clientes = ListaSimple()


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
    longitud = lista_clientes.obtenerLongitud()

    # Iterar a través de la lista enlazada para obtener los clientes
    for i in range(longitud):
        cliente = lista_clientes.obtenerNodoPorIndice(i)
        print(cliente.nombre)
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

def agregarProducto(request):
    return render(request, 'agregarProducto.html')

def agregarFactura(request):
    return render(request, 'agregarFactura.html')



# python manage.py runserver
