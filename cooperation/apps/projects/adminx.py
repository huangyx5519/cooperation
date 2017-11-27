# -*- coding: utf-8 -*-

import  xadmin

from .models import project


class projectAdmin(object):
    list_display = ['id','name', 'desc']
    search_fields = ['id', 'name', 'desc']
    list_filter = ['id', 'name', 'desc']


xadmin.site.register(project,projectAdmin)

