#coding:utf-8
from django.db import models

# Create your models here.

TIPO_FILME = [
      
      ('T','Terror'),
      ('A','Ação'),
      ('S','Suspense'),
      ('C','Comedia'),
      ('P','Policial'),
      ('I','Infantil'),
      ('R','Romantico'),
      ('D','Documentario'),
      

]
CATEGORIA = [
      
      ('S','Super Lançamento'),
      ('L','Lançamento'),
      ('P','Promoção'),
     

class filme (models.models):
	nomefilme = models.CharField('Titulo Filme:',max_length=100,null=True)
	generofilme = models.CharField('Genero do Filme:',max_length=1,choices=TIPO_FILME,null=True)
	duracaofilme = models.IntegerField('Duracao do filme',null=True, help_text="Informar duração em minutos")
	categoriafilmes= models.CharField('Categoria do Filme:',max_length=1,choices=CATEGORIA,null=True)
	def __unicode__(self):
		return self.nomefilme

class valor(models.Model):
	categoria = models.ForeignKey(filmes,verbose_name="Categoiafilmes",null=True)	
	preco = models.CharField('Preco',max_length=10,null=True)	
	

		


