from django.contrib import admin

from factura.models import Factura, LineaFactura

class FacturaAdmin(admin.ModelAdmin):
    list_display = (
        'num',
        'fecha_emision',
        'cliente_nombre',
        'cliente_direccion',
    )
    date_hierarchy = 'fecha_emision'
    search_fields = ('num', 'cliente_nombre')

admin.site.register(Factura, FacturaAdmin)

class LineaFacturaAdmin(admin.ModelAdmin):
    list_display = (
        'factura',
        'nombre_producto',
        'precio_unitario',
        'unidades',
        'iva',
    )

admin.site.register(LineaFactura, LineaFacturaAdmin)
