from django.http import request
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate


from factura.models import Factura, LineaFactura
from factura.forms import CrearFactura
from django.db.models import Sum

def factura(request):
    facturas = Factura.objects.all()
    return render(request, 'factura/factura.html', {
        'facturas': facturas.order_by('fecha_emision'),
    })

def lineafactura(request, num_factura):
    return render(request, 'factura/lineafactura.html', {
        'factura': Factura.objects.get(pk=num_factura),
    })

def home(request):
    return render(request, 'factura/inicio.html', )    

def crear_factura(request):
    form = CrearFactura(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            nueva_factura = form.save()
            return redirect('facturas/')
    return render(request, 'factura/crear_factura.html', {'form':form})   
