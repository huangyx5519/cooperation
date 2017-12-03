# -*- coding: utf-8 -*-

# from django.contrib.auth.models import User, Group
from  .models import UserProfile
from rest_framework import serializers


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        # fields = ('nick_name', 'gender', 'address', 'mobile', 'image', 'username',)
        fields = "__all__"

