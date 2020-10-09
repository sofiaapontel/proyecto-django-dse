from django.contrib import admin
#from .models import Localizacion, Producto, Categoria, Proveedor
from .models import *

# Register your models here.
admin.site.register(Localizacion)
admin.site.register(Producto)
admin.site.register(Categoria)
admin.site.register(Proveedor)
admin.site.register(Usuario)
admin.site.register(Cliente)
admin.site.register(Colaborador)
admin.site.register(Pedido)
admin.site.register(DetallePedido)
