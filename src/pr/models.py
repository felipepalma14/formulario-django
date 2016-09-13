# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible, force_text



from django.db import models

# Create your models here.

class Loja(models.Model):
	nome = models.CharField(max_length=100,null=False)

	def __unicode__(self):
		return self.nome

class Formulario(models.Model):
	LEGENDA_CHOICES = (
		('Outros','Outros'),
		('Preço Elevado','Preço Elevado'),
		('Ruptura','Ruptura'),
		('Produto Indisponivel','Produto Indisponivel'),
		('Loja','Loja'),
		('Embalagem','Embalagem'),
		('Sugestão','Sugestão'),
		('Atendimento','Atendimento'),
		('Variedade de Produtos','Variedade de Produtos'),
		('Qualidade de Produtos','Qualidade de Produtos')
		)
	cliente = models.CharField(max_length=100,null=False)
	comentario = models.TextField()
	legenda = models.CharField(choices = LEGENDA_CHOICES,default='-'),
	nota = models.PositiveSmallIntegerField()
	data = models.DateField(auto_now_add=True)
	loja = models.ForeignKey(Loja)

	def __unicode__(self):
		return self.cliente		