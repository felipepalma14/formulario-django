from django.shortcuts import render
from rest_framework import viewsets
from .models import Loja,Formulario
from .serializers import LojaSerializer,FormularioSerializer
# Create your views here.

class LojaViewSet(viewsets.ModelViewSet):
	queryset = Loja.objects.all()
	serializer_class = LojaSerializer


class FormularioViewSet(viewsets.ModelViewSet):
	queryset = Formulario.objects.all()
	serializer_class = FormularioSerializer