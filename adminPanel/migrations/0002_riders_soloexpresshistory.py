# -*- coding: utf-8 -*-
# Generated by Django 1.11.21 on 2019-06-28 00:10
from __future__ import unicode_literals

import django.contrib.postgres.fields.jsonb
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adminPanel', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='riders',
            name='soloExpressHistory',
            field=django.contrib.postgres.fields.jsonb.JSONField(default={'NA': 'NA'}),
            preserve_default=False,
        ),
    ]