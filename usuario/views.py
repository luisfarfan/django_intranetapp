from django.http import JsonResponse
from .serializer import *
from rest_framework.views import APIView
from rest_framework import generics, viewsets
from .models import Usuario
from usuario_modulo.models import Modulo, ModuloRolPermisos
from usuario_modulo.serializer import ModuloSerializer
from rest_framework.decorators import detail_route, list_route
from rest_framework.response import Response
import datetime
from django.contrib.sessions.backends.db import SessionStore
from django.contrib.sessions.models import Session
import uuid


class UserApi(object):
    def authenticate(request):
        if request.is_ajax():
            usuario = request.POST['usuario']
            clave = request.POST['clave']
            user = Usuario.objects.filter(usuario=usuario, clave=clave)

            if user:
                user_data = list(user.values()[:1])
                for i in user_data:
                    i['fecha_nacimiento'] = i['fecha_nacimiento'].strftime("%d/%m/%Y")
                    i['fecha_contrato_inicio'] = i['fecha_contrato_inicio'].strftime("%d/%m/%Y")
                    i['fecha_contrato_fin'] = i['fecha_contrato_fin'].strftime("%d/%m/%Y")
                    if i['fecha_contrato_extended'] is not None:
                        i['fecha_contrato_extended'] = i['fecha_contrato_extended'].strftime("%d/%m/%Y")

                routes = Modulo.objects.exclude(proyectosistema__isnull=True).filter(
                    modulorol__modulorolpermisos__modulorolpermisosusuario__usuario__pk=user[0].id).values('slug',
                                                                                                           'template_html')
                menu = ModuloSerializer(instance=Modulo.objects.exclude(proyectosistema__isnull=True).filter(
                    modulorol__modulorolpermisos__modulorolpermisosusuario__usuario__pk=user[0].id).distinct(),
                                        many=True).data
                token = '5'
                session = SessionStore(session_key=token)
                session['user_data'] = user_data
                session['routes'] = list(routes)
                session['menu'] = menu
                session.create()

                return JsonResponse({'user_data': user_data, 'routes': list(routes), 'menu': menu},
                                    safe=False)

    def getSession(request):
        sesion = Session.objects.get(pk=5)
        print(sesion)

        return JsonResponse({'msg': True})


class ModulosUsuarioViewSet(generics.ListAPIView):
    # queryset = Modulo.objects.all()
    serializer_class = ModuloSerializer

    def get_queryset(self):
        usuario_id = self.kwargs['usuario_id']
        return Modulo.objects.exclude(proyectosistema__isnull=True).filter(
            modulorol__modulorolpermisos__modulorolpermisosusuario__usuario__pk=usuario_id).distinct()
