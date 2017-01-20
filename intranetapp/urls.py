"""intranetapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from proyectos.urls import router_proyecto
from sistemas.urls import router_sistema
from usuario.urls import router_usuario
from django.views.generic import TemplateView

urlpatterns = []

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^rest_proyectos/', include(router_proyecto.urls)),
    url(r'^rest_sistemas/', include(router_sistema.urls)),
    url(r'^rest_usuario/', include(router_usuario.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^usuario/', include('usuario.urls', namespace='usuario')),
    url(r'^rest_proyectos/', include('proyectos.urls', namespace='proyectos')),

    url(r'^login/', TemplateView.as_view(template_name='login.html'))
]

