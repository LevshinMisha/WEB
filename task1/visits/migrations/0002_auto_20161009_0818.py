# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-10-09 03:18
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('visits', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='day',
            name='date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
