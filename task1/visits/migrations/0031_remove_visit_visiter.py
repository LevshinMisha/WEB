# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-01-12 21:11
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('visits', '0030_auto_20170113_0140'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='visit',
            name='visiter',
        ),
    ]
