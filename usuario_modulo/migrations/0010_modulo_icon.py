# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-30 02:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuario_modulo', '0009_modulo_is_padre'),
    ]

    operations = [
        migrations.AddField(
            model_name='modulo',
            name='icon',
            field=models.CharField(default='icon-home4', max_length=100),
        ),
    ]
