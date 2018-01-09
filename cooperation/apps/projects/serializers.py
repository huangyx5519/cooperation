# -*- coding: utf-8 -*-

from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from  .models import *
from users.models import UserProfile
from users.serializers import UserRegSerializer,UserProfileSimpleSerializer
from rest_framework.validators import UniqueTogetherValidator


# create（帮填） simple(权限)  默认all  扩展详情



class ReplyCreateSerializer(serializers.ModelSerializer):

    reply_people = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )

    def validate(self, attrs):
        # projectID=self.kwargs['discussion_id']
        project_belong_to_id = int(self._kwargs['context']['request']._request.path.split('/')[2])
        discussion_belong_to_id = int(self._kwargs['context']['request']._request.path.split('/')[4])
        attrs["discussion_belong_to_id"] = discussion_belong_to_id
        attrs["project_belong_to_id"] = project_belong_to_id
        return attrs

    class Meta:
        model = Reply
        fields = ("content", "discussion_belong_to_id", "project_belong_to_id", "reply_time", "reply_people",)



class ReplySerializer(serializers.ModelSerializer):
    class Meta:
        model = Reply
        fields = ("id","content", "discussion_belong_to", "reply_people", "reply_time",)



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
        fields = ("title", "desc","project_belong_to", "receiver_id","sponsor","starting_time","deadline",)


class TaskSerializer(serializers.ModelSerializer):
    sponsor = UserProfileSimpleSerializer()
    receiver = UserProfileSimpleSerializer()

    class Meta:
        model = Task
        fields = ("id","title", "desc","project_belong_to", "receiver", "sponsor", "starting_time", "deadline",)


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
    sponsor = UserProfileSimpleSerializer ()

    class Meta:
        model = Discussion
        fields = ("id","title", "project_belong_to", "desc", "sponsor",)


class FileCreateSerializer(serializers.ModelSerializer):
    # upload_people = serializers.HiddenField(
    #     default=serializers.CurrentUserDefault()
    # )

    def validate(self, attrs):
        # projectID =int(self._kwargs['context']['request']._request.path.split('/')[2])
        attrs["project_belong_to_id"] = 19
        attrs['upload_people_id']=19
        return attrs

    class Meta:
        model = File
        # fields = ("project_belong_to_id", "url","upload_people",)
        fields = ("url", "project_belong_to_id",'upload_people_id',)

class FileSerializer(serializers.ModelSerializer):
    upload_people = UserProfileSimpleSerializer()

    class Meta:
        model = File
        fields = ("id","title", "project_belong_to", "url", "upload_people",)


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


class UserProjectDetailSerializer(serializers.ModelSerializer):
    member=UserRegSerializer()
    project=ProjectSerializer()

    class Meta:
        model = UserProject
        fields = ("member","project","take_time",)




class ProjectDetailSerializer(serializers.ModelSerializer):
    files = FileSerializer(many=True)
    sponsor = UserRegSerializer()
    members = UserProjectSerializer(many=True)

    class Meta:
        model = Project
        fields = ("id", "title", "desc", "sponsor", "files","members",)
