 # -*- coding: utf-8 -*-

import  django_filters
from .models import UserProfile


class UserProfileFilter(django_filters.rest_framework.FilterSet):
    username = django_filters.CharFilter(name='username')

    class Meta:
        model = UserProfile
        fields = ['username']


class UserProjectFilter(django_filters.rest_framework.FilterSet):
    member_id = django_filters.CharFilter(name='member_id')
    member_id = django_filters.CharFilter(name='member_id')
