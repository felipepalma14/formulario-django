# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-09-21 15:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pr', '0005_auto_20160920_1744'),
    ]

    operations = [
        migrations.AlterField(
            model_name='formulario',
            name='data',
            field=models.DateField(),
        ),
    ]
