from django import template 

register = template.Library()

@register.simple_tag
def precio_total(precio_unitario, unidades):
    total = precio_unitario * unidades
    return total
 
@register.simple_tag
def importe_siniva(precio_unitario, unidades, iva):
    subimporte = precio_unitario * unidades
    impuestos = (subimporte * iva)
    return impuestos

@register.simple_tag
def importe_total(precio_unitario, unidades, iva):
    subimporte = precio_unitario * unidades
    impuestos = (subimporte * iva) 
    importe = subimporte + impuestos
    return importe

@register.simple_tag
def total(*args):
    precios = []
    for precio in args:
        precio = int(precio)
        precios.append(precio)
    return sum(precios)
    
