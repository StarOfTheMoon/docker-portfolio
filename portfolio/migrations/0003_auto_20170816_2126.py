# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-08-16 21:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_auto_20170804_0954'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='description_en',
            field=models.CharField(max_length=450, null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='description_fr',
            field=models.CharField(max_length=450, null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='subtitle_en',
            field=models.CharField(blank=True, max_length=250, null=True, verbose_name='sous titre'),
        ),
        migrations.AddField(
            model_name='project',
            name='subtitle_fr',
            field=models.CharField(blank=True, max_length=250, null=True, verbose_name='sous titre'),
        ),
        migrations.AddField(
            model_name='project',
            name='title_en',
            field=models.CharField(max_length=250, null=True, verbose_name='titre'),
        ),
        migrations.AddField(
            model_name='project',
            name='title_fr',
            field=models.CharField(max_length=250, null=True, verbose_name='titre'),
        ),
    ]
