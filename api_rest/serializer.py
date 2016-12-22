from authentication.models import *
from seguridad.models import *
from rest_framework import serializers


class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ('__all__')


class SistemaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sistema
        fields = ('__all__')


class ProyectoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proyecto
        fields = ('__all__')


class ProyectoSistemaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProyectoSistema
        fields = ('__all__')


class ModuloSerializer(serializers.ModelSerializer):
    class Meta:
        model = Modulo
        fields = ('__all__')


class PermisoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permiso
        fields = ('__all__')


class RolSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rol
        fields = ('__all__')


class ModuloPermisoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ModuloPermiso
        fields = ('__all__')


class ModuloPermisoRolSerializer(serializers.ModelSerializer):
    class Meta:
        model = ModuloPermisoRol
        fields = ('__all__')


class ModuloPermisoRolUsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = ModuloPermisoRolUsuario
        fields = ('__all__')


class TipoUsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoUsuario
        fields = ('__all__')
