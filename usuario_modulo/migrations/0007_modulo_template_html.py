# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-20 07:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuario_modulo', '0006_auto_20170120_0120'),
    ]

    operations = [
        migrations.AddField(
            model_name='modulo',
            name='template_html',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
