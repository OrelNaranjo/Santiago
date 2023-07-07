from django.contrib import admin
from .models import Proveedor, Plato, Cliente, Pedido, Repartidor, RutaEntrega, Ingrediente, CategoriaPlato

admin.site.register(Proveedor)
admin.site.register(Plato)
admin.site.register(Cliente)
admin.site.register(Pedido)
admin.site.register(Repartidor)
admin.site.register(RutaEntrega)
admin.site.register(Ingrediente)
admin.site.register(CategoriaPlato)
