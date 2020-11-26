from django import template 

register = template.Library()
 
@register.simple_tag
def importe_total(precio_unitario, unidades, iva):
    subimporte = precio_unitario * unidades
    impuestos = (subimporte * iva) 
    importe = subimporte + impuestos
    return impuestos, importe

@register.simple_tag
def total(*args):
    precios = [float(args) for args in args] 
    return precios


