import datetime
import uuid

from pymysql import *
from django.conf import settings
from rest_framework.permissions import BasePermission

from system_manage.models import ArtificialLog


class SelfPermission(BasePermission):

    def has_permission(self, request, view):
        permissions = self.get_user_permissions(request)
        # print(request.user)
        # print(request.method)
        # print(view.__class__.__name__)

        if request.method == "POST":
            category = "增加数据"
        elif request.method == "PUT":
            category = "修改数据"
        elif request.method == "DELETE":
            category = "删除数据"
        else:
            category = ""
        if category:
            try:
                object = view.serializer_class.Meta.model._meta.verbose_name
            except Exception:
                return True
            user = request.user.username
            time = datetime.datetime.now()
            ArtificialLog.objects.create(pk=uuid.uuid4(), user=user, category=category, time=time, object=object)
            # print(category, user, time, object)

        # if view.__class__.__name__ == "CompanyViewSet":
        #     if request.method == 'GET':
        #         return 'view_company' in permissions
        #     else:
        #         return 'change_company' in permissions
        # elif view.__class__.__name__ == "StaffViewSet":
        #     if request.method == 'GET':
        #         return 'view_staff' in permissions
        #     else:
        #         return 'change_staff' in permissions
        return True

    @staticmethod
    def get_user_permissions(request):
        user = request.user
        user_id = user.id
        # 如果没有登录用户为未认证类型，id为None，所以判断不为空再执行下边逻辑
        if user_id:
            permissions_all = user.groups.first().permissions.all()
            permissions = map(lambda per: per.codename, permissions_all)

        else:
            permissions = tuple()

        return permissions
