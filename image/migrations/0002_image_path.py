# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2017-04-16 05:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('image', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='path',
            field=models.TextField(default=''),
        ),
    ]
