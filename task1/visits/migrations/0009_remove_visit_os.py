# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-10-09 07:53
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('visits', '0008_visit_os'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='visit',
            name='os',
        ),
    ]