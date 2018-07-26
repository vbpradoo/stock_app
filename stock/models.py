# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models
from datetime import datetime
from django.utils.timezone import now

# # Create your models here.
# def get_default_user():
#     return User.objects.get(id=1)

class PublicLotesManager(models.Manager):

    def get_queryset(self):
        qs = super(PublicLotesManager, self).get_queryset()
        return qs


class Proovedor(models.Model):
    nombre = models.CharField(max_length=20)
    apellidos = models.CharField(max_length=40)
    correo = models.EmailField()
    telefono = models.CharField(max_length=15)
    empresa = models.CharField(max_length=20, default=None)

    class Meta:
    	ordering = ['apellidos']

    def __str__(self):
        return '%s' % (self.nombre)

class Almacenes(models.Model):
    nombre = models.CharField(max_length=20)

    def __str__(self):
        return '%s' % (self.nombre)

class Entrada(models.Model):
    fecha = models.DateTimeField()
    proovedor = models.ForeignKey(Proovedor, on_delete=models.SET_NULL, null=True)
    alamacen_entrada = models.ForeignKey(Almacenes, on_delete=models.SET_NULL, null=True)

    class Meta:
        get_latest_by = "fecha"

    def __str__(self):
        formatedDate = self.fecha.strftime("%d-%m-%Y %H")
        return 'Fecha:%s ||Almacén:%s ||Proovedor: %s ' % (formatedDate, self.alamacen_entrada, self.proovedor.nombre)


class Cliente(models.Model):
    nombre = models.CharField(max_length=20)
    apellidos = models.CharField(max_length=40)
    correo = models.EmailField()
    telefono = models.CharField(max_length=15)
    empresa = models.CharField(max_length=20, default=None)

    class Meta:
    	ordering = ['apellidos']




class Salida(models.Model):
    fecha = models.DateTimeField()
    cliente = models.ForeignKey(Cliente, on_delete=models.SET_NULL, null=True)
    cantidad = models.IntegerField()

    class Meta:
        get_latest_by = "fecha"

    def __str__(self):
        formatedDate = self.fecha.strftime("%d-%m-%Y %H")
        return 'Fecha:%s ||Cantidad:%s ||Cliente: %s ' % (formatedDate, self.cantidad, self.cliente.nombre)





class Articulo(models.Model):
    identificador = models.CharField(max_length=20)

    def __str__(self):
        return 'ID: %s' % (self.identificador)

class Movimientos(models.Model):
    origen = models.ForeignKey(Almacenes, on_delete=models.SET_NULL,  null=True, related_name='origen')
    destino = models.ForeignKey(Almacenes, on_delete=models.SET_NULL,  null=True, related_name='destino')
    fecha = models.DateTimeField()

    class Meta:
        get_latest_by = "fecha"

    def __str__(self):
        return 'Fecha: %s || Destino: %s' % (self.fecha, self.destino)


class Lotes(models.Model):
    serial = models.CharField(max_length=10, unique=True)
    articulo = models.ForeignKey(Articulo, on_delete=models.SET_NULL, null=True)
    entrada = models.ForeignKey(Entrada, on_delete=models.CASCADE)
    salida = models.ForeignKey(Salida, on_delete=models.CASCADE)
    descripcion = models.CharField(max_length=50)
    cantidad = models.IntegerField()
    unidades = models.CharField(max_length=3)
    stock = models.IntegerField()
    precio = models.IntegerField()
    movimientos = models.ForeignKey(Movimientos, on_delete=models.CASCADE)
    vendido = models.BooleanField()

    date_created = models.DateTimeField('date_created',default = now)
    date_updated = models.DateTimeField('date_updated',default = now)
    owner = models.ForeignKey(User, verbose_name='owner',related_name='lotes', on_delete = models.CASCADE)

    objects = models.Manager()
    public = PublicLotesManager()

    def __str__(self):
        return '%s (%s)' % (self.serial, self.cantidad)

    def save(self, *args, **kwargs):
        if not self.id:
            self.date_created = now()
        self.date_updated = now()   
        super(Lotes, self).save(*args, **kwargs)