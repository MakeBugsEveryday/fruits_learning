# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-10-18 15:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info_collector', '0012_synclog'),
    ]

    operations = [
        migrations.AddField(
            model_name='info',
            name='length',
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
    ]