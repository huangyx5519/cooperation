# -*- coding: utf-8 -*-

from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from  .models import *

class ProjectSerializer(serializers.ModelSerializer):
    sponsor = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = Project
        fields = ("id","title","desc","sponsor")


