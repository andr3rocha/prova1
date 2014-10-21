#coding:utf-8
from django.db import models

# Create your models here.
CONDICAO_PAGAMENTO = [

	('S','PAGO'),
	('N','NAO PAGO')
	]

class aluguel (models.Model):
	Nome = models.ForeignKey("clientes.cliente",verbose_name="Cliente",null=True)
	nomefilme = models.ForeignKey("filmes.filme",verbose_name="Filme",null=True)
	datadevolucao = models.DateField('Data Devolucao',null=True)
	pagamento = models.CharField('Pagamento',max_length=1,choices=PAGAMENTO_OPCOES,null=True)
