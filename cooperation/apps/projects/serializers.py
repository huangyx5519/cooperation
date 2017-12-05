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

class CreateUserProjectSerializer(serializers.Serializer):
    memberID = serializers.IntegerField()
    projectID = serializers.IntegerField()

    def create(self, validated_data):
        return

    # def create(self, validated_data):
    #     return True
        # member = UserProfile.objects.get(id=self.memberID)
        # project = Project.objects.get(id=self.projectID)
        # userProject = UserProject()
        # userProject.member = member
        # userProject.project = project
        # userProject.save()




    # memberID = serializers.IntegerField()
    # projectID = serializers.IntegerField()
    # member = serializers.HiddenField(
    #     default=serializers.CurrentUserDefault()
    # )
    # project = serializers.HiddenField(default=Project.objects.get(id=19))
    #
    # def validate(self, attrs):
    #     if attrs["memberID"]:
    #         attrs["member"] = UserProfile.objects.get(id=attrs["memberID"])
    #     attrs["projectID"] = Project.objects.get(id=attrs["projectID"])
    #     del attrs["memberID"]
    #     del attrs["projectID"]
    #     return attrs
    #
    # class Meta:
    #     model = UserProject
    #     fields = ("member", "project", "take_time","memberID","projectID", )


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
