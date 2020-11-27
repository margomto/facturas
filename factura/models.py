from django.db import models
from decimal import *
# Create your models here.

class Factura(models.Model): 
    num = models.AutoField(primary_key=True)
    anio = models.DateTimeField(auto_now_add=True)
    fecha_emision = models.DateTimeField(auto_now_add=True)
    cliente_nombre = models.CharField(max_length=200, verbose_name='Nombre del cliente')
    cliente_direccion = models.TextField(
        verbose_name='Dirección: ',
        max_length=100,
        )  

    def get_precio_total(self):
        getcontext().prec = 4
        total = Decimal(0)
        for linea in self.lineafactura_set.all():
            precio_item = linea.precio_real()
            total += precio_item
        return total    

    def get_iva_total(self):
        getcontext().prec = 3
        impuestos = Decimal(0)
        for linea in self.lineafactura_set.all():
            iva = linea.iva_aplicable()
            impuestos += iva
        return impuestos    

class LineaFactura(models.Model):
    factura = models.ForeignKey(
        Factura,
        on_delete=models.PROTECT,
    )
    nombre_producto = models.TextField(max_length=100)
    precio_unitario = models.DecimalField(max_digits=5, decimal_places=2)
    unidades = models.IntegerField(default=1)
    iva = models.DecimalField(max_digits=5, decimal_places=2, help_text='Indicar el I.V.A en tanto por uno', default=0.21)

    def base_imponible(self):
        return self.precio_unitario * Decimal(self.unidades)

    def iva_aplicable(self):
        return self.base_imponible() * self.iva

    def precio_real(self):
        return self.base_imponible() + self.iva_aplicable()

    
        