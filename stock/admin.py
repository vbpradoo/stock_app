# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import *

# Register your models here.


class GestionLotes(admin.ModelAdmin):
	model = Lotes
	list_display = ['serial', 'get_articulo', 'get_entrada_date', 'get_salida_date', 'descripcion']
	readonly_fields = ('date_created', 'date_updated')
#    list_editable = ('is_public',)
#    list_filter = ('entrada', 'salida','proovedor','cliente','precio')
#    search_fields = ['url', 'title', 'description']
    #readonly_fields = ('date_created', 'date_updated')
	
	def get_articulo(self, obj):
	    return obj.articulo.identificador
	    
	def get_entrada_date(self, obj):
	    return obj.entrada.fecha
	    
	def get_salida_date(self, obj):
	    return obj.salida.fecha




admin.site.register(Lotes, GestionLotes)
admin.site.register(Articulo)
admin.site.register(Cliente)
admin.site.register(Proovedor)
admin.site.register(Almacenes)
admin.site.register(Movimientos)
admin.site.register(Entrada)
admin.site.register(Salida)
