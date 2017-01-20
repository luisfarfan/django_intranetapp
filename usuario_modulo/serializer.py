from .models import *
from rest_framework import serializers


class RecursiveSerializer(serializers.Serializer):
    def to_representation(self, value):
        serializer = self.parent.parent.__class__(value, context=self.context)
        return serializer.data


class ModuloSerializer(serializers.ModelSerializer):
    modulos_hijos = RecursiveSerializer(many=True, read_only=True)

    class Meta:
        model = Modulo
        fields = ('id', 'nombre', 'descripcion', 'slug', 'codigo', 'modulo_padre', 'modulos_hijos', 'template_html')


class PermisoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permiso
        fields = ('__all__')


class RolSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rol
        fields = ('__all__')


class ModuloRolSerializer(serializers.ModelSerializer):
    permisos = PermisoSerializer(many=True, read_only=True)

    class Meta:
        model = ModuloRol
        fields = ('__all__')


class ModuloRolPermisosSerializer(serializers.ModelSerializer):
    modulorol = ModuloRolSerializer()

    class Meta:
        model = ModuloRolPermisos
        fields = ('__all__')
