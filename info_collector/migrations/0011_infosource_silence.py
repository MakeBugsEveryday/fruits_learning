# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-07-14 04:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info_collector', '0010_auto_20170708_1506'),
    ]

    operations = [
        migrations.AddField(
            model_name='infosource',
            name='silence',
            field=models.BooleanField(default=False),
        ),
    ]
