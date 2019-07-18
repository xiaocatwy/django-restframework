from django.contrib.auth.models import Group, Permission
from rest_framework import serializers

from auth_system.models import ExtraGroup


class GroupSerializer(serializers.ModelSerializer):
    note = serializers.SerializerMethodField()
    permission_ids = serializers.ListField(write_only=True)

    class Meta:
        model = Group
        fields = ["id", 'name', 'note', 'permission_ids']
        extra_kwargs = {
            "id": {"read_only": True},
            "note": {"required": False},
            "name": {"required": False},
            "permission_ids": {"required": False}
        }

    def get_note(self, obj):
        return obj.extra_group.note

    def validate_permission_ids(self, value):
        # 校验权限ids
        # 取到数据库中拥有的权限id，比较传过来的id列表是否在里面，方法是转化为集合，判断一个是否小于另一个
        value = set(value)
        ori_permission_ids = set([p.pk for p in Permission.objects.all()])
        if value <= ori_permission_ids:
            return value
        else:
            raise serializers.ValidationError("id列表中有不存在的权限id")
