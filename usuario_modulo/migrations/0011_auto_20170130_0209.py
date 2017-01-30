# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-30 07:09
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('usuario_modulo', '0010_modulo_icon'),
    ]

    operations = [
        migrations.AlterField(
            model_name='modulorol',
            name='rol',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='modulo_rol', to='usuario_modulo.Rol'),
        ),
    ]