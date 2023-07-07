from django.db import models

class Proveedor(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre
class CategoriaPlato(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Ingrediente(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Plato(models.Model):
    nombre = models.CharField(max_length=100)
    imagen = models.ImageField(upload_to='platos', default='media/platos/imagen.jpg')
    precio = models.DecimalField(max_digits=10, decimal_places=0)
    descripcion = models.TextField(default=None)
    ingredientes = models.ManyToManyField('Ingrediente')
    categoria = models.ForeignKey(CategoriaPlato, on_delete=models.CASCADE, related_name='platos', default=None)
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nombre
    
class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=100)
    saldo = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return self.nombre

class Pedido(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    platos = models.ManyToManyField(Plato)
    fecha_entrega = models.DateField()
    hora_entrega = models.TimeField()
    es_entrega_domicilio = models.BooleanField(default=False)
    entregado = models.BooleanField(default=False)

    def __str__(self):
        return f"Pedido {self.id} - Cliente: {self.cliente.nombre}"

class Repartidor(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class RutaEntrega(models.Model):
    repartidor = models.ForeignKey(Repartidor, on_delete=models.CASCADE)
    pedidos = models.ManyToManyField(Pedido)
    fecha = models.DateField()

    def __str__(self):
        return f"Ruta de entrega {self.id} - Repartidor: {self.repartidor.nombre}"
