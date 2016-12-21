from rest_framework.views import APIView
from django.http import JsonResponse
from .serializer import *
from rest_framework.views import APIView
from rest_framework import generics, viewsets
from .models import ProyectosSiga


# Create your views here.

class UsuarioViewSet(viewsets.ModelViewSet):
    serializer_class = UsuarioSerializer
    queryset = Usuario.objects.all()


class ProyectoViewSet(viewsets.ModelViewSet):
    serializer_class = ProyectoSerializer
    queryset = Proyecto.objects.all()


class SistemaViewSet(viewsets.ModelViewSet):
    serializer_class = SistemaSerializer
    queryset = Sistema.objects.all()


class ProyectoSistemaViewSet(viewsets.ModelViewSet):
    serializer_class = ProyectoSistemaSerializer
    queryset = ProyectoSistema.objects.all()


class ModuloViewSet(viewsets.ModelViewSet):
    serializer_class = ModuloSerializer
    queryset = Modulo.objects.all()


class PermisoViewSet(viewsets.ModelViewSet):
    serializer_class = PermisoSerializer
    queryset = Permiso.objects.all()


class RolViewSet(viewsets.ModelViewSet):
    serializer_class = RolSerializer
    queryset = Rol.objects.all()


class ModuloPermisoViewSet(viewsets.ModelViewSet):
    serializer_class = ModuloPermisoSerializer
    queryset = ModuloPermiso.objects.all()


class ModuloPermisoRolViewSet(viewsets.ModelViewSet):
    serializer_class = ModuloPermisoRolSerializer
    queryset = ModuloPermisoRol.objects.all()


class ModuloPermisoRolUsuarioViewSet(viewsets.ModelViewSet):
    serializer_class = ModuloPermisoRolUsuarioSerializer
    queryset = ModuloPermisoRolUsuario.objects.all()


class TipoUsuarioViewSet(viewsets.ModelViewSet):
    serializer_class = TipoUsuarioSerializer
    queryset = TipoUsuario.objects.all()


def getProyectosSiga(request):
    proyectos = list(Proyecto.objects.values_list('id_siga', flat=True))
    proyectos_disponibles = ProyectosSiga.objects.using('consecucion').exclude(id__in=proyectos).values()

    return JsonResponse(list(proyectos_disponibles), safe=False)
