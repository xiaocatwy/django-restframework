# from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets

from auth_system.models import User
from .serializers import GroupSerializer


class UserSerializer(serializers.ModelSerializer):
    groups = GroupSerializer(many=True, read_only=True)
    # groups = serializers.SerializerMethodField()
    parts = serializers.SerializerMethodField()
    # parts = PartSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ('username', 'id', 'email', 'is_active','first_name','last_name','groups', 'parts',  'default_part_id', 'default_group_id')

    # def get_groups(self, obj):
    #     return GroupSerializer(instance=obj.groups.all(), many=True, read_only=True, context={"user": obj}).data

    def get_parts(self, obj):
        #TODO 后期修改为项目在外层
        parts = obj.parts.all()
        # projects = map(lambda p: p.project, parts)  # 根据工区得到项目
        # projects = list(set(projects))  # 得到去重的列表
        return map(lambda p: {"id":p.id, "name": p.name, "project": {"project_id": p.project.id, "name": p.project.name}}, parts)
        # return map(lambda pj: {"id": pj.id, "name": pj.name, "parts": map(lambda p: {"id": p.id, "name": p.name, },set(pj.parts.all()) & set(parts))}, projects)
