from .models import *
from rest_framework import serializers


class ProyectoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proyecto
        fields = ('__all__')


class ProyectosSistemasSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProyectoSistema
        fields = ('__all__')
