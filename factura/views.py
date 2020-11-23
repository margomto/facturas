from django.http import request
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate

from factura.models import Factura, LineaFactura
from factura.forms import SignUpForm

def factura(request):
    facturas = Factura.objects.all()
    return render(request, 'factura/factura.html', {
        'facturas': facturas.order_by('fecha_emision'),
    })

def lineafactura(request, num_factura):
    elementos = LineaFactura.objects.all()
    return render(request, 'factura/lineafactura.html', {
        'elementos': elementos.order_by('precio_unitario'),
    })

def home(request):
    return render(request, 'factura/inicio.html', )    

def register(response):
    if response.method == "POST":
	    form = SignUpForm(response.POST)
	    if form.is_valid():
	        form.save()

	    return redirect("/")
    else:
	    form = SignUpForm()

    return render(response, "factura/signup.html", {"form":form})   