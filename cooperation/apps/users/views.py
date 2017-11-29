# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.

# def login(request):


# def get(self, request):
#     return render(request, "login.html", {})
#
# def post(self, request):
#     login_form = LoginForm(request.POST)
#     if login_form.is_valid():
#         username = request.POST.get("username", "")
#         password = request.POST.get("password", "")
#         user = authenticate(username=username, password=password)
#         if user is not None:
#             if user.is_active:
#                 login(request, user)
#                 return HttpResponseRedirect(reverse("index"))
#             else:
#                 return render(request, "login.html", {"msg": "用户未激活!"})
#         else:
#             return render(request, "login.html", {"msg": "用户名或密码错误!"})
#     else:
#         return render(request, "login.html", {"login_form": login_form})
