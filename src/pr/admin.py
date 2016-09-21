# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import Loja,Formulario
from .forms import FormularioForm
# Register your models here.

class FormularioAdmin(admin.ModelAdmin):
	form = FormularioForm

admin.site.site_header = 'Administração'
admin.site.register(Loja)
admin.site.register(Formulario,FormularioAdmin)