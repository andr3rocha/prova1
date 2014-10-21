#coding:utf-8
from django.db import models

CONDICAO_PAGAMENTO = [
('S','PAGO'),
('N','NAO PAGO')
]
class aluguel (models.Model):
Nome = models.ForeignKey("clientes.cliente",verbose_name="Cliente",null=True)
nomefilme = models.ForeignKey("Filme.filme",verbose_name="Filme",null=True)
datadevolucao = models.DateField('Data Devolucao',null=True)
Pagamento = models.CharField('Pagamento',max_length=1,choices=PAGAMENTO_OPCOES,null=True)
