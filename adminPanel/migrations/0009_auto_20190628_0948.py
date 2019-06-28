# -*- coding: utf-8 -*-
# Generated by Django 1.11.21 on 2019-06-28 09:48
from __future__ import unicode_literals

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminPanel', '0008_ride'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ride',
            name='requestedTime',
            field=models.DateTimeField(blank=True),
        ),
        migrations.AlterField(
            model_name='ride',
            name='source',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True),
        ),
    ]
