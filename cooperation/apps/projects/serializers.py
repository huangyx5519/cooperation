# -*- coding: utf-8 -*-

# from django.contrib.auth.models import User, Group
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.contrib.auth.hashers import make_password
from  .models import *
from users.models import UserProfile
from users.serializers import UserProfileSerializer


class UserProfileInProSerializer(serializers.ModelSerializer):


    class Meta:
        model = UserProfile
        fields = ("id",)


class ProjectSerializer(serializers.ModelSerializer):
    # sponsor = UserProfileInProSerializer()
    sponsor = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = Project
        fields = ("title","desc","sponsor")


