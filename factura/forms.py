from . import models
from django.forms import Form

from django_crispy_bulma.layout import IconField

class CrearFactura(Form):
    class Meta:
        model = models.Factura
        exclude = []
        # fields = ('num', 'anio', 'fecha_emision', 'cliente_nombre', 'cliente_direccion',)