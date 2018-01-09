 # -*- coding: utf-8 -*-

import  django_filters
from .models import *


class UserProjectFilter(django_filters.rest_framework.FilterSet):
    username = django_filters.CharFilter(name='username')

    class Meta:
        model = UserProfile
        fields = ['username']


class UserProjectFilter(django_filters.rest_framework.FilterSet):
    memberid = django_filters.CharFilter(name='member__id')
    projectid = django_filters.CharFilter(name='project__id')

    class Meta:
        model = UserProject
        fields = ['memberid','projectid']
