# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-07-14 06:15
from __future__ import unicode_literals

from django.db import migrations
import markdownx.models


class Migration(migrations.Migration):

    dependencies = [
        ('stocks', '0013_auto_20170513_0031'),
    ]

    operations = [
        migrations.AddField(
            model_name='snapshot',
            name='extra_content',
            field=markdownx.models.MarkdownxField(default='', verbose_name='\u66f4\u591a\u5185\u5bb9'),
            preserve_default=False,
        ),
    ]
