# -*- coding: utf-8 -*-

import  xadmin

from .models import Project,UserProject,Task,File,Discussion,Reply


class projectAdmin(object):
    list_display = ['id','title','desc']
    search_fields = ['id','title','desc']
    list_filter = ['id','title','desc']


xadmin.site.register(Project,projectAdmin)



class UserProjectAdmin(object):
    pass

xadmin.site.register(UserProject,UserProjectAdmin)


class FileAdmin(object):
    pass

xadmin.site.register(File,FileAdmin)

class TaskAdmin(object):
    pass

xadmin.site.register(Task,TaskAdmin)

class DiscussionAdmin(object):
    pass

xadmin.site.register(Discussion,DiscussionAdmin)

class ReplyAdmin(object):
    pass

xadmin.site.register(Reply,ReplyAdmin)
