# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-19 23:28
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('usuario', '0001_initial'),
        ('proyectos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Modulo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.TextField()),
                ('slug', models.CharField(max_length=50)),
                ('codigo', models.CharField(max_length=8)),
                ('usr_creacion', models.CharField(blank=True, max_length=100, null=True)),
                ('fec_creacion', models.DateTimeField(blank=True, null=True)),
                ('usr_edicion', models.CharField(blank=True, max_length=100, null=True)),
                ('fec_edicion', models.DateTimeField(blank=True, null=True)),
                ('modulo_padre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usuario_modulo.Modulo')),
            ],
            options={
                'db_table': 'MODULO',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='ModuloPermiso',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usr_creacion', models.CharField(blank=True, max_length=100, null=True)),
                ('fec_creacion', models.DateTimeField(blank=True, null=True)),
                ('usr_edicion', models.CharField(blank=True, max_length=100, null=True)),
                ('fec_edicion', models.DateTimeField(blank=True, null=True)),
                ('modulo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usuario_modulo.Modulo')),
            ],
            options={
                'db_table': 'MODULO_PERMISO',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='ModuloPermisoRol',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usr_creacion', models.CharField(blank=True, max_length=100, null=True)),
                ('fec_creacion', models.DateTimeField(blank=True, null=True)),
                ('usr_edicion', models.CharField(blank=True, max_length=100, null=True)),
                ('fec_edicion', models.DateTimeField(blank=True, null=True)),
                ('modulopermiso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usuario_modulo.ModuloPermiso')),
            ],
            options={
                'db_table': 'MODULO_PERMISO_ROL',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='ModuloPermisoRolUsuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usr_creacion', models.CharField(blank=True, max_length=100, null=True)),
                ('fec_creacion', models.DateTimeField(blank=True, null=True)),
                ('usr_edicion', models.CharField(blank=True, max_length=100, null=True)),
                ('fec_edicion', models.DateTimeField(blank=True, null=True)),
                ('modulopermisorol', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usuario_modulo.ModuloPermisoRol')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usuario.Usuario')),
            ],
            options={
                'db_table': 'MODULO_PERMISO_ROL_USUARIO',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Permiso',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.TextField()),
                ('codigo', models.CharField(max_length=8)),
                ('dom_name_sufijo', models.CharField(max_length=100)),
                ('usr_creacion', models.CharField(blank=True, max_length=100, null=True)),
                ('fec_creacion', models.DateTimeField(blank=True, null=True)),
                ('usr_edicion', models.CharField(blank=True, max_length=100, null=True)),
                ('fec_edicion', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'PERMISO',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Rol',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.TextField()),
                ('codigo', models.CharField(max_length=8)),
                ('usr_creacion', models.CharField(blank=True, max_length=100, null=True)),
                ('fec_creacion', models.DateTimeField(blank=True, null=True)),
                ('usr_edicion', models.CharField(blank=True, max_length=100, null=True)),
                ('fec_edicion', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'ROL',
                'managed': True,
            },
        ),
        migrations.AddField(
            model_name='modulopermisorol',
            name='rol',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usuario_modulo.Rol'),
        ),
        migrations.AddField(
            model_name='modulopermiso',
            name='permiso',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usuario_modulo.Permiso'),
        ),
        migrations.AddField(
            model_name='modulopermiso',
            name='roles',
            field=models.ManyToManyField(through='usuario_modulo.ModuloPermisoRol', to='usuario_modulo.Rol'),
        ),
        migrations.AddField(
            model_name='modulo',
            name='permisos',
            field=models.ManyToManyField(through='usuario_modulo.ModuloPermiso', to='usuario_modulo.Permiso'),
        ),
        migrations.AddField(
            model_name='modulo',
            name='proyectosistema',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='proyectos.ProyectoSistema'),
        ),
        migrations.AlterUniqueTogether(
            name='modulopermisorolusuario',
            unique_together=set([('usuario', 'modulopermisorol')]),
        ),
        migrations.AlterUniqueTogether(
            name='modulopermisorol',
            unique_together=set([('modulopermiso', 'rol')]),
        ),
        migrations.AlterUniqueTogether(
            name='modulopermiso',
            unique_together=set([('permiso', 'modulo')]),
        ),
    ]
