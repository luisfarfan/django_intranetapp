from django.db import models


# Create your models here.

class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    dni = models.CharField(max_length=8, blank=True, null=True)
    ape_pat = models.CharField(max_length=50, blank=True, null=True)
    ape_mat = models.CharField(max_length=50, blank=True, null=True)
    nombre = models.CharField(max_length=50, blank=True, null=True)
    fecha_contrato_inicio = models.DateField()
    fecha_contrato_extended = models.DateField()
    fecha_contrato_fin = models.DateField()
    fecha_nacimiento = models.DateField()
    email_inst = models.CharField(max_length=100, blank=True, null=True)
    email_personal = models.CharField(max_length=100, blank=True, null=True)
    usuario = models.CharField(max_length=50)
    clave = models.CharField(max_length=100)

    class Meta:
        managed = True
        db_table = 'USUARIO'


class UsuariosOnline(models.Model):
    id_usuario_online = models.AutoField(primary_key=True)
    usuarios = models.ForeignKey('Usuario')
    navegador_detalle = models.CharField(max_length=255, blank=True, null=True)
    ip = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'USUARIO_ONLINE'
