#coding:utf-8
from django.contrib import admin
from models import filmes


class SubEventoInline(admin.TabularInline):
	model = SubEvento


#class EventoAdmin(admin.ModelAdmin)
class filmesAdmin(admin.ModelAdmin):
	list_display = ['nomefilme','generofilme','duracaofilme']
	list_filter = ['nomefilme','generofilme']
	search_fields = ['nomefilme','generofilme']
	save_as = True
	
	
	

# Register your models here.
admin.site.register(filmes,filmesAdmin)	

