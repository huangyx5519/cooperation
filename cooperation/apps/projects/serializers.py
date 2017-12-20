# -*- coding: utf-8 -*-

from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from  .models import *
from users.models import UserProfile
from users.serializers import UserRegSerializer
from rest_framework.validators import UniqueTogetherValidator


# create（帮填） simple(权限)  默认all  扩展详情


class TaskCreateSerializer(serializers.ModelSerializer):
    receiver_id = serializers.IntegerField()

    sponsor = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )

    def validate(self, attrs):
        projectID =int(self._kwargs['context']['request']._request.path.split('/')[2])
        attrs["project_belong_to_id"] = projectID
        return attrs

    class Meta:
        model = Task
        fields = ("title", "project_belong_to_id", "receiver_id","sponsor","starting_time","deadline",)


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = "__all__"


class DiscussionCreateSerializer(serializers.ModelSerializer):
    sponsor = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )

    def validate(self, attrs):
        projectID =int(self._kwargs['context']['request']._request.path.split('/')[2])
        attrs["project_belong_to_id"] = projectID
        return attrs

    class Meta:
        model = Discussion
        fields = ("title", "project_belong_to_id", "desc","sponsor",)


class DiscussionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Discussion
        fields = "__all__"


class FileCreateSerializer(serializers.ModelSerializer):
    upload_people = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )

    def validate(self, attrs):
        projectID =int(self._kwargs['context']['request']._request.path.split('/')[2])
        attrs["project_belong_to_id"] = projectID
        return attrs

    class Meta:
        model = File
        fields = ("title", "project_belong_to_id", "url","upload_people",)


class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = "__all__"


class UserProjectSerializer(serializers.ModelSerializer):
    member_id=serializers.IntegerField()
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


class UserProjectDetailSerializer(serializers.ModelSerializer):
    member=UserRegSerializer()

    class Meta:
        model = UserProject
        fields = ("member","project","take_time",)


class ProjectCreateSerializer(serializers.ModelSerializer):
    sponsor = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = Project
        fields = ("id","title","desc","sponsor",)


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
