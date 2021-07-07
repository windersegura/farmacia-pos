from django.db import models
import uuid
# Create your models here.

class Marca(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    codigo = models.CharField(verbose_name="Coigo", max_length=50)
    numero = models.IntegerField(verbose_name="Numero", default=0)
    nombre = models.CharField(verbose_name="Nombre" ,max_length=500)
    descripcion = models.CharField(verbose_name="Nombre", max_length=500)
    creado = models.DateTimeField(verbose_name="Creado", auto_now_add=True, null=True, blank=True)
    modificado = models.DateTimeField(verbose_name="Modificado", auto_now=True, null=True, blank=True)

    def __str__(self):
        return '%s %s %s' %(self.codigo, self.nombre, self.descripcion)

    class Meta:
        db_table = 'inventario_marca'
        managed = True
        verbose_name = 'marca'
        verbose_name_plural = 'marcas'



class Producto(models.Model):
    id = models.UUIDField(primary_key=True, default= uuid.uuid4)
    codigo = models.CharField(verbose_name="Codigo", max_length=50)
    numero = models.IntegerField(verbose_name="Numero", default=0)
    nombre = models.CharField(verbose_name="Nombre", max_length=500)
    stock = models.IntegerField(verbose_name="Stock", default=0)
    precio = models.DecimalField(verbose_name="Precio", max_digits=5, decimal_places=2, default=0)
    marca= models.ForeignKey(Marca, verbose_name="Marca", on_delete=models.CASCADE)
    habilitado = models.BooleanField(verbose_name="Habilitado", default=True)
    creado = models.DateTimeField(verbose_name="Creado", auto_now_add=True, null=True, blank=True)
    modificado = models.DateTimeField(verbose_name="Modificado", auto_now=True, null=True, blank=True)

    def __str__(self):
        return '%s %s %s' %(self.codigo, self.nombre, self.stock)

    class Meta:
        db_table = 'inventario_producto'
        managed = True
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'


class Presentacion(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    codigo = models.CharField(verbose_name="Codigo", max_length=50)
    numero = models.IntegerField(verbose_name="Numero", default=0)
    nombre = models.CharField(verbose_name="Nombre", max_length=500)
    unidades = models.IntegerField(verbose_name="Unidades", default=0)
    unidad_medida = models.CharField(verbose_name="Unidad Medida", max_length=50)
    creado = models.DateTimeField(verbose_name="Creado", auto_now_add=True, null=True, blank=True)
    modificado = models.DateTimeField(verbose_name="Modificado", auto_now=True, null=True, blank=True)
    producto = models.ForeignKey(Producto, verbose_name="Producto", on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        pass

    class Meta:
        db_table = 'inventario_presentacion'
        managed = True
        verbose_name = 'pesentacion'
        verbose_name_plural = 'presentaciones'

