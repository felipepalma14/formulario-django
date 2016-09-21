from django import forms
from .models import Formulario




class FormularioForm(forms.ModelForm):
	legenda = forms.MultipleChoiceField(choices=Formulario.LEGENDA_CHOICES, widget=forms.CheckboxSelectMultiple())
	data = forms.DateField(widget = forms.DateInput(format=('%d/%m/%Y'), 
                                    attrs={'class':'Formulario', 
                                    'placeholder':'dd/mm/yyyy'}))
	class Meta:
		model = Formulario
		fields=('cliente','comentario','legenda','nota','data','loja',)
		#exclude = ('data',)