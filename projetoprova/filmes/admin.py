#coding:utf-8
from django.contrib import admin
from models import filme
from modesl import valores


class filmeAdmin(admin.ModelAdmin):
	list_display = ['nomefilme','generofilme','duracaofilme']
	list_filter = ['nomefilme','generofilme']
	search_fields = ['nomefilme','generofilme']
	save_as = True
	
class valoreAdmin(admin.ModelAdmin):
	list_display = ['categoria','preco']
	list_filter = ['categoria','preco']
	search_fields = ['categoria','preco']
	save_as = True
	
	

# Register your models here.
admin.site.register(filmes,filmesAdmin)	
admin.site.register(valores,valoresAdmin)
