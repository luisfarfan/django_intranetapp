from django.db import models


# Create your models here.
class Proyecto(models.Model):
    id_siga = models.IntegerField()
    nombre = models.CharField(max_length=100)
    sigla = models.CharField(max_length=50, null=True, blank=True)
    anio = models.IntegerField()
    descripcion = models.TextField(blank=True, null=True)
    fecha_inicio = models.DateField(blank=True, null=True)
    fecha_fin = models.DateField(blank=True, null=True)
    cod_meta = models.CharField(max_length=8)
    estado = models.IntegerField(default=1)
    usr_creacion = models.CharField(max_length=100, blank=True, null=True)
    fec_creacion = models.DateTimeField(blank=True, null=True)
    usr_edicion = models.CharField(max_length=100, blank=True, null=True)
    fec_edicion = models.DateTimeField(blank=True, null=True)
    sistemas = models.ManyToManyField('Sistema', through='ProyectoSistema')

    class Meta:
        managed = True
        db_table = 'PROYECTO'
        unique_together = (('id_siga',))


class Sistema(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    codigo = models.CharField(max_length=8)
    usr_creacion = models.CharField(max_length=100, blank=True, null=True)
    fec_creacion = models.DateTimeField(blank=True, null=True)
    usr_edicion = models.CharField(max_length=100, blank=True, null=True)
    fec_edicion = models.DateTimeField(blank=True, null=True)
    estado = models.IntegerField(default=1)

    class Meta:
        managed = True
        db_table = 'SISTEMA'


class ProyectoSistema(models.Model):
    proyectos = models.ForeignKey('Proyecto')
    sistemas = models.ForeignKey('Sistema')
    usr_creacion = models.CharField(max_length=100, blank=True, null=True)
    fec_creacion = models.DateTimeField(blank=True, null=True)
    usr_edicion = models.CharField(max_length=100, blank=True, null=True)
    fec_edicion = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'PROYECTO_SISTEMA'
        unique_together = (('proyectos', 'sistemas'))


class Modulo(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    slug = models.CharField(max_length=50)
    codigo = models.CharField(max_length=8)
    proyectosistema = models.ForeignKey('ProyectoSistema')
    usr_creacion = models.CharField(max_length=100, blank=True, null=True)
    fec_creacion = models.DateTimeField(blank=True, null=True)
    usr_edicion = models.CharField(max_length=100, blank=True, null=True)
    fec_edicion = models.DateTimeField(blank=True, null=True)
    modulo_padre = models.ForeignKey('Modulo')
    permisos = models.ManyToManyField('Permiso', through='ModuloPermiso')

    class Meta:
        managed = True
        db_table = 'MODULO'


class Permiso(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    codigo = models.CharField(max_length=8)
    dom_name_sufijo = models.CharField(max_length=100)
    usr_creacion = models.CharField(max_length=100, blank=True, null=True)
    fec_creacion = models.DateTimeField(blank=True, null=True)
    usr_edicion = models.CharField(max_length=100, blank=True, null=True)
    fec_edicion = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'PERMISO'


class ModuloPermiso(models.Model):
    permiso = models.ForeignKey('Permiso')
    modulo = models.ForeignKey('Modulo')
    roles = models.ManyToManyField('Rol', through='ModuloPermisoRol')
    usr_creacion = models.CharField(max_length=100, blank=True, null=True)
    fec_creacion = models.DateTimeField(blank=True, null=True)
    usr_edicion = models.CharField(max_length=100, blank=True, null=True)
    fec_edicion = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'MODULO_PERMISO'
        unique_together = (('permiso', 'modulo'))


class Rol(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    codigo = models.CharField(max_length=8)
    usr_creacion = models.CharField(max_length=100, blank=True, null=True)
    fec_creacion = models.DateTimeField(blank=True, null=True)
    usr_edicion = models.CharField(max_length=100, blank=True, null=True)
    fec_edicion = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'ROL'


class ModuloPermisoRol(models.Model):
    modulopermiso = models.ForeignKey('ModuloPermiso')
    rol = models.ForeignKey('Rol')
    usr_creacion = models.CharField(max_length=100, blank=True, null=True)
    fec_creacion = models.DateTimeField(blank=True, null=True)
    usr_edicion = models.CharField(max_length=100, blank=True, null=True)
    fec_edicion = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'MODULO_PERMISO_ROL'
        unique_together = (('modulopermiso', 'rol'))
