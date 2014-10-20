#coding:utf-8
from django.contrib import admin
from models import filmes
from modesl import valores


class filmesAdmin(admin.ModelAdmin):
	list_display = ['nomefilme','generofilme','duracaofilme']
	list_filter = ['nomefilme','generofilme']
	search_fields = ['nomefilme','generofilme']
	save_as = True
	
class valoresAdmin(admin.ModelAdmin):
	list_display = ['Categoria','Preco']
	list_filter = ['Categoria','Preco']
	search_fields = ['Categoria','Preco']
	save_as = True
	
	

# Register your models here.
admin.site.register(filmes,filmesAdmin)	
admin.site.register(valores,valoresAdmin)
