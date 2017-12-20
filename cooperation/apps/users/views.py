# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import MySQLdb
from rest_framework.views import APIView

from .models import UserProfile
from rest_framework import viewsets
from .serializers import UserProfileSerializer,UserRegSerializer
from rest_framework import filters
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAdminUser
from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet
from rest_framework.response import Response
from rest_framework.authtoken.admin import TokenAdmin
from rest_framework import status

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
    # permission_classes = (IsAdminUser,)
    pagination_class = UserProfilePagination
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    filter_class = UserProfileFilter
    search_fields = ('username',)
    ordering_fields = ('username',)

class UserSignUpViewset(mixins.CreateModelMixin, GenericViewSet):
    """
    用户
    """
    queryset = UserProfile.objects.all()
    serializer_class = UserRegSerializer

class getMyId(APIView):
    def get(self, request,format=None):
        try:
            token=request.META['HTTP_AUTHORIZATION'].split()[1]

            conn = MySQLdb.connect(
                host='localhost',
                port=3306,
                user='root',
                passwd='',
                db='cooperationDB',
            )
            cur = conn.cursor()
            userid = cur.execute("select user_id from authtoken_token where authtoken_token.key='%s'" % (token))
            userid = cur.fetchall()[0][0]
            cur.close()
        except Exception, e:
            return Response(status=status.HTTP_401_UNAUTHORIZED)

        return Response(userid)


# class MyViewset(mixins.ListModelMixin,GenericViewSet):
#     authentication_classes = (TokenAuthentication,)
#     queryset = UserProfile.objects.all()
#     serializer_class=MySerializer
#
#     def get_queryset(self):
#         return UserProfile.objects.filter(id=self.request.user.id)










