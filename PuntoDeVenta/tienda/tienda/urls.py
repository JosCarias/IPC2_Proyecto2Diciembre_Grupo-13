"""
URL configuration for tienda project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import views

urlpatterns = [
    path('hello/', views.hello_world, name='hello_world'),
    path('test/', views.test_page_view, name='test_page'),
    path('', views.index, name='index'),
    path('Cliente/', views.agregarCliente, name='agregar_cliente'),
    path('Cliente/clientes/', views.listar_clientes, name='ver_clientes'),
    path('Producto/', views.agregar_producto, name='agregar_Producto'),
    path('Producto/productos/', views.listar_productos, name='ver_Producto'),
    path('Venta/', views.agregar_factura, name='agregar_Factura'),
    path('Venta/ventas/', views.listar_facturas, name='ver_Factura'),
    path('estadisca/', views.estadisca, name='estadisca'),
]

# python manage.py runserver