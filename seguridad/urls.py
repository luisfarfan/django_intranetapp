from django.conf.urls import url
from django.views.generic import TemplateView

urlpatterns = [
    url(r'^proyectos/', TemplateView.as_view(template_name='seguridad/proyectos.html')),
    url(r'^sistemas/', TemplateView.as_view(template_name='seguridad/sistemas.html')),
]
