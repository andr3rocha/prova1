#coding:utf-8
from django.db import models

# Create your models here.

TIPO_FILME = [
      
      ('A','Terror'),
      ('B','Ação'),
      ('C','Aventura'),
      ('D','Suspense'),
      ('E','Comedia'),
      ('F','Policial'),
      ('G','Infantil'),
      ('H','Romantico'),
      ('I','Documentario'),
      

]
CATEGORIA = [
      
      ('A','Super Lançamento'),
      ('B','Lançamento'),
      ('C','Promoção'),
     

class filmes (models.filmes):
	nomefilme = models.CharField('Titulo Filme:',max_length=100,null=True)
	generofilme = models.CharField('Genero do Filme:',max_length=1,choices=TIPO_FILME,null=True)
	duracaofilme = models.IntegerField('Duracao do filme',null=True, help_text="Informar duração em minutos")
	categoriafilme = models.CharField('Categoria do Filme:',max_length=1,choices=CATEGORIA,null=True)
	
	class Meta:
		verbose_name = "Macro filme"
		verbose_name_plural = "Macro filme"
	
	def __unicode__(self):
		return self.nomefilme


