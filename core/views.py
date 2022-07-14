from dataclasses import dataclass
from pickletools import read_uint1
from django.shortcuts import render, redirect,get_object_or_404
from core.models import producto
from .forms import contactoForm, productoForm
from django.contrib import messages
from django.core.paginator import Paginator
from django.http import Http404
from rest_framework import viewsets
from.serializers import producto_Serializer

class productoViewset(viewsets.ModelViewSet):
    queryset = producto.objects.all()
    serializer_class= producto_Serializer


# Create your views here.

def home(request):
    return render(request,'core/home.html')

def productos(request):
    productos=producto.objects.all()
    data = {
        'productos':productos
    }
    return render(request,'core/productos.html',data)

def quienes(request):
    return render(request,'core/quienes.html')

def contacto(request):
    data = {
        'form': contactoForm()
    }
    if request.method == 'POST':
        formulario = contactoForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"]="contacto enviado"




    return render(request,'core/contacto.html',data) 
    

def adopcion(request):
    return render(request,'core/adopcion.html')

def login(request):
    return render(request,'core/login.html')

def agregar_producto(request):
    
    data={
        'form':productoForm()
    }
    if request.method == 'POST':
        formulario = productoForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request,"Producto ingresado exitosamente!")
        else:
            data["form"] = formulario

    return render(request,'core/producto/agregar.html',data)

def listar_productos(request):
    product = producto.objects.all()
    page = request.GET.get('page',1)
    
    try:
        paginator = Paginator(product,8)
        product  = paginator.page(page)
    except:
        raise Http404



    data = {
        'productos':product,
        'paginator': paginator
    }
 

    return render(request, 'core/producto/listar.html',data)

def modificar_producto(request, id):

    productos = get_object_or_404(producto, id=id)
    
    data = {
        'form' : productoForm(instance=productos)
    }

    if request.method == 'POST':
        formulario=productoForm(data=request.POST, instance=productos, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request,"Producto modificado exitosamente!")
            return redirect(to="listar_productos")
        data["form"] = formulario


    return render(request,'core/producto/modificar.html',data)

def eliminar_producto(request, id):
    Producto = get_object_or_404(producto,id=id)
    Producto.delete()
    messages.success(request,"Producto eliminado exitosamente!")
    return redirect(to="listar_productos")