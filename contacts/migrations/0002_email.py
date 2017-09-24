# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-09-24 06:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Email',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=256)),
                ('sender', models.CharField(max_length=256)),
                ('content', models.TextField(blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('is_mailed', models.BooleanField(default=False)),
                ('mailed_at', models.DateTimeField(blank=True, null=True)),
                ('recipients', models.ManyToManyField(related_name='sent_emails', to='contacts.Contact')),
            ],
        ),
    ]
