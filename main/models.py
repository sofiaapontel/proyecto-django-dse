from django.db import models

# Create your models here.
class Proveedor(models.Model):
    ruc = models.CharField(max_length=11)
    razon_social = models.CharField(max_length=20)
    telefono = models.CharField(max_length=9)

    def _str_(self):
        return self.razon_social

class Categoria(models.Model):
    codigo = models.CharField(max_length=4)
    nombre = models.CharField(max_length=50)

    def _str_(self):
        return f'{self.codigo}: {self.nombre}'

class Localizacion(models.Model):
    distrito = models.CharField(max_length=20)
    provincia = models.CharField(max_length=20)
    departamento = models.CharField(max_length=20)

    def _str_ (self):
        return f'{self.distrito}, {self.provincia}, {self.departamento}'

class Usuario(models.Model):
    email = models.EmailField(max_length=30)
    password = models.CharField(max_length=20)
    documentoIdentidad = models.CharField(max_length=8)
    nombres = models.CharField(max_length=20)
    apellidoPaterno = models.CharField(max_length=20)
    apellidoMaterno = models.CharField(max_length=20)
    genero = models.CharField(max_length=10)
    fechaNacimiento = models.DateField()
    fechaCreacion = models.DateField()
    estado = models.CharField(max_length=20)

    def _str_(self):
        return f'{self.documentoIdentidad}: {self.apellidoPaterno} {self.apellidoMaterno}, {self.nombres}'

##----------------------------------------------------------
class Cliente(Usuario):
    preferencias = models.CharField(max_length=20)

    def _str_(self):
        return self.email

##----------------------------------------------------------
class Colaborador(Usuario):
    reputacion = models.FloatField()
    # Relaciones
    coberturaEntrega = models.ForeignKey('Localizacion', on_delete=models.SET_NULL, null=True)
    #crear método de crearCuenta()

    def calcularReputacion(self):
        return sum(self.reputacion)

    def _str_(self):
        return f'{self.apellidoPaterno} {self.apellidoMaterno}, {self.nombres}'

class Producto(models.Model):
    #atributos
    nombre = models.CharField(max_length=20)
    descripcion = models.TextField()
    precio = models.FloatField()
    estado = models.CharField(max_length=3)
    descuento = models.FloatField(default=0)
    # Relaciones
    categoria = models.ForeignKey('Categoria', on_delete=models.SET_NULL, null=True)
    proveedor = models.ForeignKey('Proveedor', on_delete=models.SET_NULL, null=True)

    def _str_(self):
        return self.nombre

    def precio_final(self):
        return self.precio * (1 - self.descuento)

    def sku(self):
        codigo_categoria = self.categoria.codigo.zfill(4)
        codigo_producto = str(self.id).zfill(6)
        #unir en cadena
        return f'{codigo_categoria}-{codigo_producto}'

class Pedido(models.Model):
    fechaCreacion = models.DateField()
    estado = models.CharField(max_length=20)
    fechaEntrega = models.DateField()
    direccionEntrega = models.CharField(max_length=20)
    tarifa = models.FloatField()
    # Relaciones
    cliente = models.ForeignKey('Cliente', on_delete=models.SET_NULL, null=True)
    repartidor = models.ForeignKey('Colaborador', on_delete=models.SET_NULL, null=True)
    ubicacion = models.ForeignKey('Localizacion', on_delete=models.SET_NULL, null=True)

    def calcularTarifa(self):
        return self.tarifa

    def _str_(self):
        return f'{self.estado}, {self.repartidor}'

class DetallePedido(models.Model):
    cantidad = models.IntegerField()
    subtotal = models.FloatField()
    # Relaciones
    pedido = models.ForeignKey('Pedido', on_delete=models.SET_NULL, null=True)
    producto = models.ForeignKey('Producto', on_delete=models.SET_NULL, null=True)

    def calcularSubtotal(self):
        return sum(self.subtotal)
