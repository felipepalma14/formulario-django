from .models import Formulario,Loja
from rest_framework import serializers



class LojaSerializer(serializers.ModelSerializer):
	class Meta:
		model = Loja
		fields = ('nome',)

class FormularioSerializer(serializers.ModelSerializer):
	loja = serializers.CharField(read_only=True,source = 'loja.nome') 
	legenda = serializers.MultipleChoiceField(Formulario.LEGENDA_CHOICES)
	class Meta:
		model = Formulario
		fields = ('cliente' ,'comentario','legenda','nota','data','loja')
	