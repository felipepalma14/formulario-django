# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-09-20 17:44
from __future__ import unicode_literals

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('pr', '0004_auto_20160920_1728'),
    ]

    operations = [
        migrations.AlterField(
            model_name='formulario',
            name='legenda',
            field=multiselectfield.db.fields.MultiSelectField(choices=[(1, 'Outros'), (2, 'Preco Elevado'), (3, 'Ruptura'), (4, 'Produto Indisponivel'), (5, 'Loja'), (6, 'Embalagem'), (7, 'Sugestao'), (8, 'Atendimento'), (9, 'Variedade de Produtos'), (10, 'Qualidade de Produtos')], default='-', max_length=30),
        ),
    ]
