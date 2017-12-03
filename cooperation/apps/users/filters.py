 # -*- coding: utf-8 -*-

import  django_filters
from .models import UserProfile


class UserProfileFilter(django_filters.rest_framework.FilterSet):
    username = django_filters.CharFilter(name='username',lookup_expr='icontains')

    class Meta:
        model = UserProfile
        fields = ['username']


