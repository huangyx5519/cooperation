# -*- coding: utf-8 -*-

from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from  .models import *
from users.models import UserProfile
from users.serializers import UserRegSerializer


class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = ("title",)

class UserProjectSerializer(serializers.ModelSerializer):
    member=UserRegSerializer()

    class Meta:
        model = UserProject
        fields = ("member","project","take_time",)


#list 显示
class ProjectSerializer(serializers.ModelSerializer):
    sponsor = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = Project
        fields = ("id","title","desc","sponsor",)


#re 显示

class ProjectDetailSerializer(serializers.ModelSerializer):
    files = FileSerializer(many=True)
    sponsor = UserRegSerializer()
    members = UserProjectSerializer(many=True)

    class Meta:
        model = Project
        fields = ("id", "title", "desc", "sponsor", "files","members",)
