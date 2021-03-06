# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-29 06:22
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userproject',
            name='member',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='\u9879\u76ee\u6210\u5458'),
        ),
        migrations.AddField(
            model_name='userproject',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.Project', verbose_name='\u9879\u76ee'),
        ),
        migrations.AddField(
            model_name='task',
            name='project_belong_to',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.Project', verbose_name='\u6240\u5c5e\u9879\u76ee'),
        ),
        migrations.AddField(
            model_name='task',
            name='receiver',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='receiver', to=settings.AUTH_USER_MODEL, verbose_name='\u63a5\u6536\u8005'),
        ),
        migrations.AddField(
            model_name='task',
            name='sponsor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sponsor', to=settings.AUTH_USER_MODEL, verbose_name='\u53d1\u8d77\u8005'),
        ),
        migrations.AddField(
            model_name='reply',
            name='discussion_belong_to',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.Discussion', verbose_name='\u6240\u5c5e\u8ba8\u8bba'),
        ),
        migrations.AddField(
            model_name='reply',
            name='project_belong_to',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.Project', verbose_name='\u6240\u5c5e\u9879\u76ee'),
        ),
        migrations.AddField(
            model_name='project',
            name='sponsor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='\u9879\u76ee\u8d1f\u8d23\u4eba'),
        ),
        migrations.AddField(
            model_name='file',
            name='project_belong_to',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.Project', verbose_name='\u6240\u5c5e\u9879\u76ee'),
        ),
        migrations.AddField(
            model_name='file',
            name='upload_people',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='\u4e0a\u4f20\u8005'),
        ),
        migrations.AddField(
            model_name='discussion',
            name='project_belong_to',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.Project', verbose_name='\u6240\u5c5e\u9879\u76ee'),
        ),
        migrations.AddField(
            model_name='discussion',
            name='sponsor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='\u53d1\u8d77\u8005'),
        ),
    ]
