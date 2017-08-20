# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-08-20 07:28
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Diary',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='DiaryContent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.IntegerField(null=True)),
                ('title', models.CharField(blank=True, max_length=128)),
                ('content_attr', models.CharField(max_length=20)),
            ],
            options={
                'ordering': ['order'],
            },
        ),
        migrations.CreateModel(
            name='DiaryImage',
            fields=[
                ('diarycontent_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='diary.DiaryContent')),
                ('image', models.ImageField(upload_to='diary')),
            ],
            bases=('diary.diarycontent',),
        ),
        migrations.CreateModel(
            name='DiaryText',
            fields=[
                ('diarycontent_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='diary.DiaryContent')),
                ('text', models.TextField()),
            ],
            bases=('diary.diarycontent',),
        ),
        migrations.AddField(
            model_name='diarycontent',
            name='diary',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contents', to='diary.Diary'),
        ),
    ]
    