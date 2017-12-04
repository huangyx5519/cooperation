# -*- coding: utf-8 -*-

# from django.contrib.auth.models import User, Group
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.contrib.auth.hashers import make_password
from  .models import *

from users.serializers import UserProfile

class ProjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = Project
        fields = "__all__"

#
# class ProjectSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Project
#         fields = "__all__"
#
#
# class ProjectSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Project
#         fields = "__all__"
#
#
# class ProjectSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Project
#         fields = "__all__"

