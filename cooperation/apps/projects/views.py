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
    # search_fields = ('title',)
    # search_fields= ('sponsor__id',)
    #外键属性双下划线，这里应该使用fiter更好，后面改
    ordering_fields = ('create_time',)


    def get_serializer_class(self):
        if self.action == "retrieve":
            return ProjectDetailSerializer
        return ProjectSerializer



class UserProjectViewset(mixins.CreateModelMixin, mixins.ListModelMixin, mixins.RetrieveModelMixin,
                     mixins.DestroyModelMixin, viewsets.GenericViewSet):
    """
    list:
        获取用户项目关系
    retrieve:
        判断某个项目已经参加
    create:
        加入
    """
    queryset = UserProject.objects.all()
    permission_classes = (IsAuthenticated, TakePartInPermission)
    authentication_classes = (TokenAuthentication,)
    # lookup_field = "goods_id"

    def get_queryset(self):
        return UserProject.objects.filter(member=self.request.user)

    def get_serializer_class(self):
        if self.action == "create":
            return CreateUserProjectSerializer
        return UserProjectSerializer
