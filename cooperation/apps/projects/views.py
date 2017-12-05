# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import viewsets
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAdminUser
from rest_framework.permissions import IsAuthenticated

from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet
from .models import *
from .serializers import *
from utils.permissions import ProjectPermission,TakePartInPermission


# 展示

class ProjectViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Project.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (ProjectPermission,)
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    filter_fields = ("sponsor__id",)
    ordering_fields = ('create_time',)


    def get_serializer_class(self):
        #获取详情
        if self.action == "retrieve":
            return ProjectDetailSerializer
        return ProjectSerializer



class UserProjectViewset(GenericViewSet,mixins.CreateModelMixin,mixins.DestroyModelMixin,mixins.ListModelMixin):
    """
    list:
        获取用户项目关系
    retrieve:
        判断某个项目已经参加
    create:
        加入
    """
    queryset = UserProject.objects.all()
    # permission_classes = (IsAuthenticated, TakePartInPermission)
    authentication_classes = (TokenAuthentication,)
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    filter_fields = ("project_id","member_id",)

    # def get_queryset(self):
        # return UserProject.objects.filter(member=self.request.user)
        # return UserProject

    def get_serializer_class(self):
        if self.action == "create":
            return UserProjectSerializer
        return UserProjectDetailSerializer



class FileViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = File.objects.all()
    authentication_classes = (TokenAuthentication,)
    # permission_classes = (ProjectPermission,)
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    ordering_fields = ('upload_date',)


    def get_serializer_class(self):
        return FileSerializer


class ProjectFileViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """

    queryset = File.objects.all()
    authentication_classes = (TokenAuthentication,)
    # permission_classes = (ProjectPermission,)
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    ordering_fields = ('upload_date',)
    projectID = None

    def get_queryset(self):
        path = self.request._request.path
        self.projectID = path.split('/')[2]
        queryset = File.objects.all().filter(project_belong_to_id=self.projectID)
        return queryset

    def get_serializer_class(self):
        if self.action == "create":
            return FileCreateSerializer
        return FileSerializer


