# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-01-12 21:14
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('visits', '0031_remove_visit_visiter'),
    ]

    operations = [
        migrations.AddField(
            model_name='visit',
            name='visiter',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='visits.Visiter'),
        ),
    ]
