# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-11-24 10:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('visits', '0015_urls'),
    ]

    operations = [
        migrations.AddField(
            model_name='visit',
            name='urls_text',
            field=models.TextField(default=''),
        ),
    ]
