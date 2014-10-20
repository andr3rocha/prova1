#coding:utf-8
from django.db import models

# Create your models here.

SEXO_OPCOES = [

	('M','Masculino'),
	('F','Feminino')

]



class cliente(models.Model):
	
	Nome = models.CharField('Nome',max_length=100,null=True)
	Sexo = models.CharField('Sexo',max_length=1,choices=SEXO_OPCOES,null=True)
	CPF = models.CharField('CPF',max_length=15,null=True)
	DataNascimento = models.DateField('Data de Nascimento',null=True)
	Telefone = models.CharField('Telefone',max_length=15,null=True)
	Celular = models.CharField('Celular',max_length=15,null=True)
	Email = models.EmailField('Endereço de email',max_length=100)
	Logradouro = models.CharField('Logradouro', max_length=100,null=True)
	Numero = models.IntegerField('Número',null=True)
	Complemento = models.CharField('Complemento', max_length=100,null=True,blank=True)
	Bairro = models.CharField('Bairro', max_length=100,null=True)
	Cidade = models.CharField('Cidade', max_length=100,null=True)
 	URL = models.URLField ('Página Pessoal', max_length=200,null=True,blank=True)
 	
 	def __unicode__(self):
		return self.Nome
	
