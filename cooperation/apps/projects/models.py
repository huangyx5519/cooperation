# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from datetime import datetime
from users.models import UserProfile
# Create your models here.


class Project(models.Model):
    title = models.CharField(verbose_name=u"项目名称",max_length=50,default="")
    sponsor = models.ForeignKey(UserProfile, verbose_name=u"项目负责人")
    desc = models.CharField(verbose_name=u"项目描述",max_length=500,default="")
    create_time = models.DateTimeField(default=datetime.now, verbose_name=u"创建时间")

    class Meta:
        verbose_name = u"项目"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.title


class UserProject(models.Model):
    member = models.ForeignKey(UserProfile, verbose_name=u"项目成员")
    project = models.ForeignKey(Project, verbose_name=u"项目",related_name="members")
    take_time = models.DateTimeField(default=datetime.now, verbose_name=u"参与时间")

    class Meta:
        verbose_name = u"项目用户关联"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return u"关联"


class Task(models.Model):
    title = models.TextField(verbose_name=u"任务名称")
    desc = models.TextField(verbose_name=u"任务描述",default="")
    project_belong_to = models.ForeignKey(Project, verbose_name=u"所属项目")
    sponsor = models.ForeignKey(UserProfile, related_name='sponsor', verbose_name=u"发起者")
    receiver = models.ForeignKey(UserProfile, related_name='receiver', verbose_name=u"接收者")
    starting_time = models.DateTimeField(default=datetime.now, verbose_name=u"创建时间")
    deadline = models.DateTimeField(verbose_name=u"截止时间",null=True)
    is_end = models.BooleanField(default=False, verbose_name=u"是否结束")

    class Meta:
        verbose_name = u"任务"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.title


class File(models.Model):
    title = models.TextField(verbose_name=u"文件名称")
    project_belong_to = models.ForeignKey(Project, verbose_name=u"所属项目",related_name="files")
    url = models.FileField(upload_to="project/file/%Y/%m", verbose_name=u"资源文件", max_length=100)
    type = models.TextField(verbose_name=u"文件类型")
    upload_people = models.ForeignKey(UserProfile, verbose_name=u"上传者")
    upload_date = models.DateTimeField(default=datetime.now,verbose_name=u"上传时间时间")
    is_valid = models.BooleanField(default=True, verbose_name=u"是否有效")

    class Meta:
        verbose_name = u"文件"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.title


class Discussion(models.Model):
    title = models.TextField(verbose_name=u"讨论名称")
    desc = models.TextField(verbose_name=u"讨论描述")
    project_belong_to = models.ForeignKey(Project, verbose_name=u"所属项目")
    sponsor = models.ForeignKey(UserProfile, verbose_name=u"发起者" )
    starting_time = models.DateTimeField(default=datetime.now, verbose_name=u"创建时间")

    class Meta:
        verbose_name = u"讨论"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.title


class Reply(models.Model):
    # title = models.TextField(verbose_name=u"回复标题")
    content = models.TextField(verbose_name=u"回复内容")
    reply_time = models.DateTimeField(default=datetime.now, verbose_name=u"回复时间")
    reply_people = models.ForeignKey(UserProfile, verbose_name=u"层主",null=True)
    project_belong_to = models.ForeignKey(Project, verbose_name=u"所属项目")
    discussion_belong_to = models.ForeignKey(Discussion, verbose_name=u"所属讨论")
    # floor_place = models.IntegerField(default=1, verbose_name=u"所在楼层")

    class Meta:
        verbose_name = u"回复"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.title




