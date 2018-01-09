# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import viewsets
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.authentication import TokenAuthentication,SessionAuthentication
from rest_framework.parsers import FileUploadParser
from rest_framework.permissions import IsAdminUser
from rest_framework.permissions import IsAuthenticated

from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet
from .models import *
from .serializers import *
from utils.permissions import ProjectPermission,TakePartInPermission
from .filters import *
from rest_framework.views import APIView
from rest_framework.response import Response

# Task  Discussion  Reply

class DiscussionReplyViewSet(viewsets.ModelViewSet):
    queryset = Reply.objects.all()
    authentication_classes = (TokenAuthentication, SessionAuthentication,)
    # permission_classes = (ProjectPermission,)

    def get_queryset(self):
        discussion_id = self.kwargs['discussion_id']
        queryset = Reply.objects.all().filter(discussion_belong_to_id=discussion_id)
        return queryset

    def get_serializer_class(self):
        if self.action == "create" or self.action == "update":
            return ReplyCreateSerializer
        return ReplySerializer

class ProjectTaskViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """

    queryset = Task.objects.all()
    authentication_classes = (TokenAuthentication,SessionAuthentication,)
    # permission_classes = (ProjectPermission,)

    def get_queryset(self):
        project_id = self.kwargs['project_id']
        queryset = Task.objects.all().filter(project_belong_to_id=project_id)
        return queryset

    def get_serializer_class(self):
        if self.action == "create" or self.action == "update":
            return TaskCreateSerializer
        return TaskSerializer


class ProjectDiscussionViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """

    queryset = Discussion.objects.all()
    authentication_classes = (TokenAuthentication,)
    # permission_classes = (ProjectPermission,)
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    ordering_fields = ('upload_date',)

    def get_queryset(self):
        project_id = self.kwargs['project_id']
        queryset = Discussion.objects.all().filter(project_belong_to_id=project_id)
        return queryset

    def get_serializer_class(self):
        s =self.action
        if self.action == "create" or self.action == "update":
            return DiscussionCreateSerializer
        return DiscussionSerializer




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
        project_id = self.kwargs['project_id']
        queryset = File.objects.all().filter(project_belong_to_id=project_id)
        return queryset

    def get_serializer_class(self):
        if self.action == "create" or self.action == "update" :
            return FileCreateSerializer
        return FileSerializer


class UserProjectViewset(viewsets.ModelViewSet):
    """
    list:
        获取用户项目关系
    retrieve:
        判断某个项目已经参加
    create:
        加入
    """
    queryset = UserProject.objects.all()
    authentication_classes = (TokenAuthentication,)
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    filter_class = UserProjectFilter
    # filter_fields = ("projectid","memberid",)
    # search_fields = ("member_id","project_id")

    def get_serializer_class(self):
        if self.action == "create" or self.action == "update":
            return UserProjectSerializer
        return UserProjectDetailSerializer


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
        if self.action == "create":
            return ProjectCreateSerializer
        return ProjectSerializer

    def perform_create(self, serializer):
        project = serializer.save()
        # project.members
        sponsor = project.sponsor
        eUserProject = UserProject()
        eUserProject.member=sponsor
        eUserProject.project=project
        eUserProject.save()


class FileUploadView(APIView):
    parser_classes = (FileUploadParser,)

    def post(self, request, filename, format=None):
        # file_obj = request.FILES['file']
        print(request)
        print(request.FILES)
        return Response(status=204)

