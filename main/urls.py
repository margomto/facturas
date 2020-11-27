
from django.contrib import admin
from django.urls import path
from django.conf.urls import url


import factura.views

urlpatterns = [
    path('', factura.views.home, name="inicio"),
    path('admin/', admin.site.urls),
    path('facturas/', factura.views.factura, name="facturas"),
    path('detalle/<int:num_factura>', factura.views.lineafactura, name="detalle_factura"),
    url('nuevafactura/', factura.views.crear_factura, name="crear_factura"),
]
