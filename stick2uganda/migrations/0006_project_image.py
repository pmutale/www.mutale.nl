# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-09-22 09:32
from __future__ import unicode_literals

from django.db import migrations
import django.db.models.deletion
import filer.fields.image


class Migration(migrations.Migration):

    dependencies = [
        ('filer', '0007_auto_20161016_1055'),
        ('stick2uganda', '0005_s2uimageplugin_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='image',
            field=filer.fields.image.FilerImageField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='filer.Image'),
        ),
    ]