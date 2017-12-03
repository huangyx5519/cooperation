# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import UserProfile
from rest_framework import viewsets
from .serializers import UserProfileSerializer,UserRegSerializer
from rest_framework import filters
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.authentication import TokenAuthentication

from .filters import UserProfileFilter

# 分页
class UserProfilePagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100

class UserProfileViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = UserProfile.objects.all().order_by('-date_joined')
    serializer_class = UserProfileSerializer
    authentication_classes = (TokenAuthentication,)
    pagination_class = UserProfilePagination
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    filter_class = UserProfileFilter
    search_fields = ('username',)
    ordering_fields = ('username',)


class UserViewset(viewsets.ModelViewSet):
    """
    用户
    """
    queryset = UserProfile.objects.all()
    serializer_class = UserRegSerializer






