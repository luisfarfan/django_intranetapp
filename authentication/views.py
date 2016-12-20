from django.http import HttpResponseRedirect
from django.http import JsonResponse
from django.shortcuts import render
from django.views import View
from .models import Usuario
from django.views.decorators.csrf import csrf_exempt


# Create your views here.s
def authenticate(request):
    if request.is_ajax():
        usuario = request.POST['usuario']
        clave = request.POST['clave']
        user = Usuario.objects.filter(usuario=usuario, clave=clave)

        if user:
            return JsonResponse({'msg': True}, safe=False)
        else:
            return JsonResponse({'msg': False}, safe=False)
