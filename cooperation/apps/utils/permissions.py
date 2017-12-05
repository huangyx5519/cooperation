# -*- coding: utf-8 -*-
from rest_framework import permissions
from projects.models import UserProject

class ProjectPermission(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):

        action = view.action
        ProjectId = obj.id
        UserProjectSet = UserProject.objects.filter(project_id=ProjectId).all()
        members = [user_project.member for user_project in UserProjectSet]

        if (action=="retrieve"):
            if (request.user in members):
                return True
        if (action=="list"):
            return True

        # return obj.sponsor == request.user
        return False


