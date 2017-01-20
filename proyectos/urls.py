from rest_framework import routers
from django.conf.urls import url
from .views import *
from django.contrib.sessions.backends.db import SessionStore
from django.contrib.sessions.models import Session

routing_session = SessionStore()

router_proyecto = routers.DefaultRouter()
router_proyecto.register(r'proyecto', ProyectoViewSet)
router_proyecto.register(r'proyecto_sistema', ProyectoSistemaViewSet)

urlpatterns = [
    url(r'getProyectosSiga', ProyectosApi.getProyectosSiga),
    url(r'saveProyectoSistema', ProyectosApi.saveProyectoSistema),
]

session_key = routing_session.session_key
session_exist = Session.objects.filter(pk=session_key)
if session_exist:
    session = Session.objects.get(pk=session_key)
    session_decoded = session.get_decoded()

    if 'menu' in session_decoded:
        for menu in session_decoded['menu']:
            if menu['is_padre'] == 0:
                urlpatterns.append(
                    url(r'^' + menu['slug'] + '/', TemplateView.as_view(template_name=menu['template_html'])))
