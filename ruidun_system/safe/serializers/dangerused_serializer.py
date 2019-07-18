import uuid

from rest_framework import serializers
from ..models import DangerUsed, Danger, DangerousCategory
from staff.models import Staff


class DangerSerializer(serializers.ModelSerializer):
    """危险品模型"""

    category = serializers.SlugRelatedField(label='分类名称', slug_field='name', read_only=True)

    class Meta:
        model = Danger
        exclude = ('create_time', 'update_time', 'count')


class DangerUsedSerializer(serializers.ModelSerializer):
    """危险物品管理序列化器"""

    id = serializers.CharField(label='使用记录编号',  read_only=True)
    danger_id = serializers.CharField(label='危险品编号', allow_null=True, write_only=True)
    # danger = serializers.SlugRelatedField(slug_field='name',read_only=True)
    danger = DangerSerializer(required=False)
    manager_id = serializers.CharField(label='负责人id', allow_null=True)
    manager = serializers.SlugRelatedField(label='负责人', slug_field='name', read_only=True)
    user_id = serializers.CharField(label='使用人id', allow_null=True, max_length=50)
    user = serializers.SlugRelatedField(label='使用人', slug_field='name', read_only=True)

    class Meta:
        model = DangerUsed
        exclude = ('create_time', 'update_time')

    def validate_danger_id(self, value):
        if Danger.objects.filter(pk=value).count() == 0:
            raise serializers.ValidationError("危险品不存在")
        return value

    def validate_manager(self, value):
        # 查看人员表中，是否存在该用户
        if Staff.objects.filter(name=value).count() == 0:
            raise serializers.ValidationError("负责人不存在")
        return value

    def validate_user(self, value):
        # 查看人员表中，是否存在该用户
        if Staff.objects.filter(name=value).count() == 0:
            raise serializers.ValidationError("使用人不存在")
        return value

    def create(self, validated_data):
        """新建"""
        pk = uuid.uuid4()
        return DangerUsed.objects.create(pk=pk, **validated_data)

    def update(self, instance, validated_data):
        """更新，instance为要更新的对象实例"""
        instance.danger_id = validated_data.get('danger_id', instance.danger_id)
        instance.manager_id = validated_data.get('manager_id', instance.manager)
        instance.user_id = validated_data.get('user_id', instance.user)
        instance.count = validated_data.get('count', instance.count)
        instance.is_need_back = validated_data.get('is_need_back', instance.is_need_back)
        instance.is_back = validated_data.get('is_back', instance.is_back)
        instance.start_time = validated_data.get('start_time', instance.start_time)
        instance.end_time = validated_data.get('end_time', instance.end_time)
        instance.save()
        return instance