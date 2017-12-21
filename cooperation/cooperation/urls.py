# -*- coding: utf-8 -*-

from django.conf.urls import url, include
from rest_framework import routers
from rest_framework.documentation import include_docs_urls
from rest_framework.authtoken import views as authviews
from users import views as userView
from projects import views as projectView
import xadmin

# from django.contrib import admin
router = routers.DefaultRouter()
router.register(r'myinfo', userView.MyViewSet)
router.register(r'users', userView.UserProfileViewSet)
router.register(r'signup', userView.UserSignUpViewset)
router.register(r'project', projectView.ProjectViewSet)
router.register(r'userproject', projectView.UserProjectViewset)

projectRouter = routers.DefaultRouter()
projectRouter.register(r'file', projectView.ProjectFileViewSet)
projectRouter.register(r'task', projectView.ProjectTaskViewSet)
# projectRouter.register(r'member', projectView.ProjectMemberViewSet)
projectRouter.register(r'discussion', projectView.ProjectDiscussionViewSet)

urlpatterns = [
    url(r'^getid/$', userView.getMyId.as_view()),     #获取用户id
    url(r'^signin/', authviews.obtain_auth_token),
    url(r'^project/(?P<project_id>\d+)/', include(projectRouter.urls)),
    url(r'^', include(router.urls)),
    url(r'docs/',include_docs_urls(title="cooperation")),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api-token-auth/', authviews.obtain_auth_token),
    url(r'^xadmin/', xadmin.site.urls),
]


