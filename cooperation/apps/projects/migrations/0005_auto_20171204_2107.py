# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-04 13:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0004_auto_20171204_2104'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='desc',
            field=models.CharField(default='', max_length=500, verbose_name='\u9879\u76ee\u63cf\u8ff0'),
        ),
        migrations.AddField(
            model_name='project',
            name='title',
            field=models.CharField(default='', max_length=50, verbose_name='\u9879\u76ee\u540d\u79f0'),
        ),
    ]