from rest_framework import routers
from .views import *
from django.conf.urls import url
from .views import *

router = routers.DefaultRouter()
router.register(r'usuarios', UsuarioViewSet)
router.register(r'proyectos', ProyectoViewSet)
router.register(r'sistemas', SistemaViewSet)
router.register(r'proyectosistemas', ProyectoSistemaViewSet)
router.register(r'modulos', ModuloViewSet)
router.register(r'permisos_modulo', ModuloPermisoViewSet)
router.register(r'permisos', PermisoViewSet)
router.register(r'roles', RolViewSet)
router.register(r'modulo_permiso_rol', ModuloPermisoRolViewSet)
router.register(r'usuarios_detalle', ModuloPermisoRolUsuarioViewSet)
router.register(r'tipo_usuario', TipoUsuarioViewSet)

# router.register(r'pea_cursocriterio', PEA_CURSOCRITERIOViewSet)


urlpatterns = [
    url(r'getProyectosSiga', getProyectosSiga),
    url(r'saveProyectoSistema', saveProyectoSistema),
]
