# -*- coding: utf-8 -*-

from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from  .models import *
from users.models import UserProfile
from users.serializers import UserRegSerializer
from rest_framework.validators import UniqueTogetherValidator

class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = "__all__"

class UserProjectDetailSerializer(serializers.ModelSerializer):
    member=UserRegSerializer()

    class Meta:
        model = UserProject
        fields = ("member","project","take_time",)


class UserProjectSerializer(serializers.ModelSerializer):
    member_id = serializers.IntegerField()
    project_id = serializers.IntegerField()

    class Meta:
        model = UserProject
        validators = [
            UniqueTogetherValidator(
                queryset=UserProject.objects.all(),
                fields=('project_id', 'member_id'),
                message="已经参加"
            )
        ]
        fields = ("take_time","member_id","project_id",)


class ProjectSerializer(serializers.ModelSerializer):
    sponsor = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = Project
        fields = ("id","title","desc","sponsor",)


class ProjectDetailSerializer(serializers.ModelSerializer):
    files = FileSerializer(many=True)
    sponsor = UserRegSerializer()
    members = UserProjectSerializer(many=True)

    class Meta:
        model = Project
        fields = ("id", "title", "desc", "sponsor", "files","members",)
