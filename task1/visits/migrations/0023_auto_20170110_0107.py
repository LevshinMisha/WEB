# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-01-09 20:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('visits', '0022_visit_screen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='visit',
            name='screen',
            field=models.TextField(default='JS или куки былы выключены'),
        ),
    ]
