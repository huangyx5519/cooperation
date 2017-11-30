# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import UserProfile
from rest_framework import viewsets
from .serializers import UserProfileSerializer


class UserProfileViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = UserProfile.objects.all().order_by('-date_joined')
    serializer_class = UserProfileSerializer
