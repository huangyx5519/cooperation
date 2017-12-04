"""cooperation URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.conf.urls import url, include
from rest_framework import routers
from rest_framework.documentation import include_docs_urls
from rest_framework.authtoken import views as authviews
from users import views
import xadmin

# from django.contrib import admin
router = routers.DefaultRouter()
router.register(r'users', views.UserProfileViewSet)
router.register(r'signup', views.UserSignUpViewset)



urlpatterns = [
    url(r'^signin/', authviews.obtain_auth_token),
    url(r'^api-token-auth/', authviews.obtain_auth_token),
    url(r'^xadmin/', xadmin.site.urls),
    url(r'^', include(router.urls)),
    url(r'docs/',include_docs_urls(title="cooperation")),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
    # url(r'^users/', include('users.urls', namespace='users')),
    # url(r'^cooperation/', include('cooperation.urls', namespace='cooperation')),
]
