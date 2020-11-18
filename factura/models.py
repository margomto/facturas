from django.db import models
from django.db.models import Sum
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

class LineaFactura(models.Model):
    factura = models.ForeignKey(
        Factura,
        on_delete=models.PROTECT,
    )
    nombre_producto = models.TextField(max_length=100)
    precio_unitario = models.DecimalField(max_digits=5, decimal_places=2)
    unidades = models.IntegerField(default=1)
    iva = models.DecimalField(max_digits=5, decimal_places=2, help_text='Indicar el I.V.A en tanto por uno', default=0.21)

    
        
    
        