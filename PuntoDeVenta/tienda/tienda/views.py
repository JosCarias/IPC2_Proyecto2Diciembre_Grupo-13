from django.http import HttpResponse
from django.shortcuts import render
from tienda.Back.cliente import *
from tienda.Back.producto import *
from tienda.Back.factura import *
from tienda.Back.lista_simple import *
import matplotlib.pyplot as plt
import io
import urllib, base64


lista_clientes = ListaSimple()
lista_productos = ListaSimple()
lista_facturas = ListaSimple()


def hello_world(request):
    return HttpResponse("<h1>Hello world</h1>")

def test_page_view(request):
    return render(request, 'test_page.html')

def index(request):
    return render(request, 'index.html')

def estadistica(request):
    # Lógica para la primera gráfica (productos más vendidos)
    x_productos = []
    y_productos = []

    elementos_productos = lista_productos.cantidadElementos()

    if elementos_productos > 0:
        for i in range(elementos_productos):
            numeroVentas = int(lista_productos.BuscarPorIndice(i).cantidadVentas)
            producto = lista_productos.BuscarPorIndice(i).nombre
            if numeroVentas > 0:
                x_productos.append(producto)
                y_productos.append(numeroVentas)

    fig_productos, ax_productos = plt.subplots()
    ax_productos.plot(x_productos, y_productos)
    plt.title('Productos más vendidos')
    plt.xlabel('Nombre producto')
    plt.ylabel('Cantidad vendida')

    # Guardar la gráfica de productos más vendidos como imagen
    buffer_productos = io.BytesIO()
    plt.savefig(buffer_productos, format='png')
    buffer_productos.seek(0)
    image_png_productos = buffer_productos.getvalue()
    buffer_productos.close()

    # Convertir la imagen de productos a base64
    graphic_productos = base64.b64encode(image_png_productos).decode('utf-8')
    image_productos = "data:image/png;base64," + graphic_productos

    # Lógica para la segunda gráfica (clientes con más productos)
    x_clientes = []
    y_clientes = []

    elementos_clientes = lista_facturas.cantidadElementos()

    if elementos_clientes > 0:
        for i in range(elementos_clientes):
            numeroProductos = lista_facturas.BuscarPorIndice(i).productos.cantidadElementos()
            nombreCliente = lista_facturas.BuscarPorIndice(i).nombre
            if numeroProductos > 0:
                x_clientes.append(nombreCliente)
                y_clientes.append(numeroProductos)

    fig_clientes, ax_clientes = plt.subplots()
    ax_clientes.plot(x_clientes, y_clientes)
    plt.title('Clientes con más productos')
    plt.xlabel('Nombre cliente')
    plt.ylabel('Cantidad productos comprados')

    # Guardar la gráfica de clientes con más productos como imagen
    buffer_clientes = io.BytesIO()
    plt.savefig(buffer_clientes, format='png')
    buffer_clientes.seek(0)
    image_png_clientes = buffer_clientes.getvalue()
    buffer_clientes.close()

    # Convertir la imagen de clientes a base64
    graphic_clientes = base64.b64encode(image_png_clientes).decode('utf-8')
    image_clientes = "data:image/png;base64," + graphic_clientes

    return render(request, 'verGraficas.html', {'image_productos': image_productos, 'image_clientes': image_clientes})



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

def editar_producto(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        id = request.POST.get('id')
        descripcion = request.POST.get('descripcion')
        precio = request.POST.get('precio')
        stock = request.POST.get('stock')

        producto_existente = lista_productos.BuscarPorNombre(nombre)
        if producto_existente:
            # Modificar los atributos del producto existente
            producto_existente.nombre = nombre
            producto_existente.id = id
            producto_existente.descripcion = descripcion
            producto_existente.precio = precio
            producto_existente.stock = stock

            return render(request, 'editarProducto.html')  # Página de éxito o redirección

    return render(request, 'editarProducto.html')



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
                    if factura.productos.obtenerNodoPorIndice(j):

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

def eliminar_factura(request):
    if request.method == 'GET':
        nombre = request.GET.get('nombre')
        lista_facturas.EliminarPorNombre(nombre) # Eliminar la factura de la lista

        return render(request, 'eliminarFactura.html')  # Renderiza una página de éxito o redirige a otra vista

def editar_factura(request):
    if request.method == 'POST':
        nombreAnterior = request.POST.get('nombreAnterior')
        numero = request.POST.get('numeroFactura')
        nuevoNombre = request.POST.get('nombreCliente')  # Ajustar el nombre del campo según el formulario
        nit = lista_clientes.BuscarPorNombre(nuevoNombre).nit
        total = request.POST.get('total')
        nombreProducto = request.POST.get('productos')
        allProducto = nombreProducto.split(',')
        
        factura = lista_facturas.BuscarPorNombre(nombreAnterior)

        if factura:
            # Se asignan los nuevos datos
            lista_facturas.EditarPorNombreFactura(nombreAnterior,numero,nit,nuevoNombre,total)

            # Se encarga de contabilizar la cantidad de productos anteriores en la factura
            productosEnFactura = lista_facturas.BuscarPorNombre(nuevoNombre).productos.cantidadElementos()

            # Vaciamos el listado de productos anteriores en la factura
            while productosEnFactura != 0:
                productoAEliminar = lista_facturas.BuscarPorNombre(nuevoNombre).productos.BuscarPorIndice(0).nombre
                lista_facturas.EliminarProductoEnFactura(nuevoNombre,productoAEliminar)
                productosEnFactura = productosEnFactura -1

            # Agregamos los nuevos productos
            for unProducto in allProducto:
                busquedaProducto = lista_productos.BuscarPorNombre(unProducto)
                if busquedaProducto:
                    busquedaProducto.cantidadVentas += 1
                    lista_facturas.insertarEnFactura(nuevoNombre,busquedaProducto)

        return render(request, 'editarFactura.html')
    return render(request, 'editarFactura.html')

def buscar_cliente(request):
    if request.method == 'POST':
        nombre_cliente = request.POST.get('id')  
        cliente = lista_clientes.BuscarPorNombre(nombre_cliente)   

        # Verificar si el cliente se encontró
        if cliente:

            return render(request, 'buscarCliente.html', {'cliente': cliente})
        else:
            mensaje_error = f"No se encontró ningun cliente con el nombre: {nombre_cliente}"
            return render(request, 'buscarCliente.html', {'error_message': mensaje_error})

    return render(request, 'buscarCliente.html')


def buscar_producto(request):
    if request.method == 'POST':
        nombre_producto = request.POST.get('id')  
        producto = lista_productos.BuscarPorNombre(nombre_producto)   

        # Verificar si el cliente se encontró
        if producto:

            return render(request, 'buscarProducto.html', {'producto': producto})
        else:
            mensaje_error = f"No se encontró ningun producto con el nombre: {nombre_producto}"
            return render(request, 'buscarCliente.html', {'error_message': mensaje_error})

    return render(request, 'buscarProducto.html')


def eliminar_producto(request):
    if request.method == 'GET':
        nombre = request.GET.get('nombre')
        lista_productos.EliminarPorNombre(nombre) # Eliminar el producto de la lista

        return render(request, 'eliminarProducto.html')


# python manage.py runserver
