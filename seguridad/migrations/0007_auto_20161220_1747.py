# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-12-20 22:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seguridad', '0006_auto_20161220_1745'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proyecto',
            name='descripcion',
            field=models.TextField(blank=True, null=True),
        ),
    ]
