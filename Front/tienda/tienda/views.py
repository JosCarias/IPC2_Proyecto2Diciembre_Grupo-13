from django.http import HttpResponse
from django.shortcuts import render

def hello_world(request):
    return HttpResponse("<h1>Hello world</h1>")

def test_page_view(request):
    return render(request, 'test_page.html')

def index(request):
    return render(request, 'index.html')

def agregarCliente(request):
    return render(request, 'agregarCliente.html')

def agregarProducto(request):
    return render(request, 'agregarProducto.html')

def agregarFactura(request):
    return render(request, 'agregarFactura.html')