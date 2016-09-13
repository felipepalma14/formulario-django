from django.contrib import admin
from .models import Loja,Formulario
from .forms import FormularioForm
# Register your models here.

class FormularioAdmin(admin.ModelAdmin):
	form = FormularioForm


admin.site.register(Loja)
admin.site.register(Formulario,FormularioAdmin)