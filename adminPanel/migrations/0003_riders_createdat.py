# -*- coding: utf-8 -*-
# Generated by Django 1.11.21 on 2019-06-28 07:48
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('adminPanel', '0002_riders_soloexpresshistory'),
    ]

    operations = [
        migrations.AddField(
            model_name='riders',
            name='createdAt',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
