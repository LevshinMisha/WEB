# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-01-13 01:32
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('visits', '0025_auto_20170113_0018'),
    ]

    operations = [
        migrations.AlterField(
            model_name='visit',
            name='last_hit',
            field=models.DateTimeField(default=datetime.datetime(2017, 1, 13, 7, 32, 39, 848946)),
        ),
    ]