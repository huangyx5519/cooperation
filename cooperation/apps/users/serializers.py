# -*- coding: utf-8 -*-

# from django.contrib.auth.models import User, Group
from  .models import UserProfile
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.contrib.auth.hashers import make_password


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = "__all__"


class UserRegSerializer(serializers.ModelSerializer):
    username = serializers.CharField(label="用户名", help_text="用户名", required=True, allow_blank=False,
                                     validators=[UniqueValidator(queryset=UserProfile.objects.all(), message="用户已经存在")])
    password = serializers.CharField(
        style={'input_type': 'password'},help_text="密码", label="密码", write_only=True,
    )


    def validate(self, attrs):
        attrs["password"] = make_password(attrs["password"])
        return attrs

    class Meta:
        model = UserProfile
        fields = ("username", "password")
