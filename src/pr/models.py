# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible, force_text
from multiselectfield import MultiSelectField
from vitello import settings
from django.db import models

# Create your models here.


class Loja(models.Model):
	nome = models.CharField(max_length=100,null=False)
	#formulario = models.ForeignKey(Formulario,related_name='formulario')

	def __unicode__(self):
		return self.nome

class Formulario(models.Model):
	LEGENDA_CHOICES = (
		(1,'Outros'),
		(2,'Preco Elevado'),
		(3,'Ruptura'),
		(4,'Produto Indisponivel'),
		(5,'Loja'),
		(6,'Embalagem'),
		(7,'Sugestao'),
		(8,'Atendimento'),
		(9,'Variedade de Produtos'),
		(10,'Qualidade de Produtos')
		)
	cliente = models.CharField(max_length=100,null=False)
	comentario = models.TextField()
	legenda = MultiSelectField(choices = LEGENDA_CHOICES,default='-',max_length=30)
	nota = models.PositiveSmallIntegerField()
	data = models.DateField()
	loja = models.ForeignKey(Loja)

	def __unicode__(self):
		return self.cliente		

