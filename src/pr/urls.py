from django.conf.urls import url,include
from rest_framework import routers
from .views import LojaViewSet,FormularioViewSet


router = routers.DefaultRouter()
router.register(r'loja',LojaViewSet)
router.register(r'formulario',FormularioViewSet)