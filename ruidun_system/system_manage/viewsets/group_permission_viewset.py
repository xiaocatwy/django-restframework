from django.contrib.auth.models import Group, Permission
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response

from auth_system.models import ExtraGroup, ContentTypeCat
from lib.model_viewset import ModelViewSet
from system_manage.serializers.extra_group_serializer import ExtraGroupSerializer
from system_manage.serializers.group_serializer import GroupSerializer
# from system_manage.serializers.permission_serializer import PermissionSerializer


class GroupPermissionViewSet(ModelViewSet):
    """对角色基本信息及相关权限进行设置的视图"""

    queryset = Group.objects.filter(extra_group__is_used=1).all()

    def get_serializer_class(self):
        # if self.request.method == "GET":
        return GroupSerializer

    @action(methods=["GET"], detail=True)
    def get_group_permission(self, request, pk):
        obj = self.get_object()
        # 获取当前组所拥有的权限
        permissions = Permission.objects.filter(group=obj.id).all().order_by('content_type_id')
        # serializer = PermissionSerializer(permissions, many=True)
        # return Response(data=serializer.data, status=status.HTTP_200_OK)
        data = self.serializer_permission(permissions)
        return Response(data=data, status=status.HTTP_200_OK)

    @action(methods=["GET"], detail=False)
    def get_all_permission(self, request):
        # 获取所有的权限
        permissions = Permission.objects.all().order_by('content_type_id')
        # serializer = PermissionSerializer(permissions, many=True)
        # return Response(data=serializer.data, status=status.HTTP_200_OK)
        data = self.serializer_permission(permissions)
        return Response(data=data, status=status.HTTP_200_OK)

    def serializer_permission(self, permissions):
        # 通过权限来得到权限的分类及权限的序列化信息
        permissions = set(permissions)
        content_types = map(lambda p: p.content_type, permissions)
        content_types = list(set(content_types))  # 得到去重的列表
        return map(lambda ct: {"id": ct.id, "name": ct.model, "permissions": map(lambda p: {"id": p.id, "name": p.name, },
                                                                          set(ct.permission_set.all()) & permissions)}, content_types)
        # return map(lambda ct: {"id": ct.id, "name": ct.model,
        #                        "permissions": map(lambda p: {"id": p.id, "name": p.name, },
        #                                           set(ct.permission_set.all()) & permissions)}, content_types)

        # return map(lambda ct: {
        #     "cat_name": ContentTypeCat.objects.filter(
        #         id=ct.content_type_cat_rel.all().values('content_type_cat_id')[0]['content_type_cat_id']).values('name')[0][
        #         'name'] if ct.content_type_cat_rel.all() else ""},
        #            content_types)

    def retrieve(self, request, *args, **kwargs):
        # 获取单个角色的基本信息，该角色的权限，以及所有的权限
        obj = self.get_object()
        serializer = self.get_serializer(obj)
        # 基本的角色信息
        data = serializer.data
        # 该角色所拥有的权限
        permissions = Permission.objects.filter(group=obj.id).all().order_by('content_type_id')
        # serializer = PermissionSerializer(permissions, many=True)
        # data["permissions"] = serializer.data
        data["self_permissions"] = self.serializer_permission(permissions)
        # 所有的权限提供给修改使用
        total_permissions = Permission.objects.all().order_by('content_type_id')
        # serializer = PermissionSerializer(total_permissions, many=True)
        # data["total_permissions"] = serializer.data
        data["total_permissions"] = self.serializer_permission(total_permissions)
        return Response(data=data, status=status.HTTP_200_OK)

    def create(self, request, *args, **kwargs):
        extra, group_data = self.check_data(request.data)
        # 创建角色及相关及权限
        group = Group.objects.create(name=group_data["name"])
        group.permissions.set(group_data["permission_ids"])
        group.save()
        # 创建用户附加信息
        extra = ExtraGroup.objects.create(group_id=group.pk, **extra)
        extra.save()
        return Response(data=GroupSerializer(group).data, status=status.HTTP_201_CREATED)

    def check_data(self, data):
        # 校验角色额外信息数据
        extra = dict()
        # data = dict(data)
        extra["note"] = data.get("note")
        extra["is_used"] = data.get("is_used", 1)
        extra["index"] = data.get("index", 1)
        serializer = ExtraGroupSerializer(data=extra)
        serializer.is_valid(raise_exception=True)
        extra = serializer.data

        # 校验角色数据
        group_data = dict()
        permissions = data.get("permission_ids")
        # group_data["permission_ids"] = eval(permissions) if permissions else None
        group_data["permission_ids"] = permissions if permissions else []
        if data.get("name"):
            group_data["name"] = data.get("name")
        serializer = GroupSerializer(data=group_data)
        serializer.is_valid(raise_exception=True)
        # group_data = serializer.data

        return extra, group_data

    def update(self, request, *args, **kwargs):
        group = self.get_object()
        extra_group = group.extra_group
        if request.data.get("name") == group.name:
            del request.data["name"]
        extra, group_data = self.check_data(request.data)
        extra_group.note = extra["note"]
        extra_group.is_used = extra["is_used"]
        extra_group.index = extra["index"]
        extra_group.save()
        group.name = group_data.get('name', group.name)
        if group_data.get("permission_ids"):
            group.permissions.set(group_data["permission_ids"])
        group.save()
        return Response(data=GroupSerializer(group).data, status=status.HTTP_205_RESET_CONTENT)

    def destroy(self, request, *args, **kwargs):
        group = self.get_object()
        group.extra_group.is_used = 0
        group.extra_group.save()
        return Response(data={"message": "删除成功"}, status=status.HTTP_204_NO_CONTENT)

