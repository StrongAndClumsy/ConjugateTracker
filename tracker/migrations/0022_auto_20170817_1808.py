# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-08-18 01:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0021_merge_20170817_1749'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deadliftmovement',
            name='created_at',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='squatmovement',
            name='created_at',
            field=models.DateTimeField(),
        ),
    ]
