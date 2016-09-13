from django import forms
from .models import Formulario




class FormularioForm(forms.ModelForm):
	legenda = forms.MultipleChoiceField(choices=Formulario.LEGENDA_CHOICES, widget=forms.CheckboxSelectMultiple())

	class Meta:
		model = Formulario
		exclude = ('data',)