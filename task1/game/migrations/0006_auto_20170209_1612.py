# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-02-09 16:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0005_auto_20170209_1612'),
    ]

    operations = [
        migrations.AlterField(
            model_name='choice',
            name='text',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='choice',
            name='title',
            field=models.CharField(blank=True, max_length=30),
        ),
    ]