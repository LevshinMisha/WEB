# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-10-09 06:03
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('extuser', '0004_extuser_visits_count'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='extuser',
            name='visits_count',
        ),
    ]
