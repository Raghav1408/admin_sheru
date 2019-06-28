# -*- coding: utf-8 -*-
# Generated by Django 1.11.21 on 2019-06-28 08:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminPanel', '0004_auto_20190628_0800'),
    ]

    operations = [
        migrations.AlterField(
            model_name='riders',
            name='emailId',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='riders',
            name='fcmToken',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='riders',
            name='firstName',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='riders',
            name='lastName',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='riders',
            name='paymentPreference',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='riders',
            name='picture',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='riders',
            name='rating',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='riders',
            name='referralMoney',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='riders',
            name='referredBy',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='riders',
            name='state',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='riders',
            name='status',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='riders',
            name='walletId',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]