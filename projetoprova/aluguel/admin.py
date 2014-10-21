
#coding:utf-8

from django.contrib import admin
from models import aluguel

#class FilmesInline(admin.TabularInline):
# model = aluguel

class aluguelAdmin(admin.ModelAdmin):
list_display = ['nome','nomefilme','datadevolucao','pagamento']
list_filter = ['nome']
search_fields = ['nome']
save_as = True

