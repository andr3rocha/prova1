#coding:utf-8
from django.contrib import admin
from models import clientes


# Register your models here.

class clienteAdmin(admin.ModelAdmin):
	list_display = ['Nome','CPF']
	list_filter = ['Sexo']
	search_fields = ['Nome','CPF']
	
admin.site.register(clientes,clientesAdmin)
