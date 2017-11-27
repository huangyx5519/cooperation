# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class project(models.Model):

    name = models.CharField(max_length=50, verbose_name=u"项目名称")
    desc = models.TextField(verbose_name=u"项目描述")


    class Meta:
        verbose_name = u"项目"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name
