# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-04 03:44
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('weibo_backup', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tweet',
            options={'ordering': ['-published']},
        ),
    ]