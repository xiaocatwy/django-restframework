import uuid
from rest_framework import serializers
from ..models import DangerousCategory


class DangerousCategorySerializer(serializers.ModelSerializer):
    """危险物品分类序列化器（搜索字段）"""

    # id = serializers.IntegerField(read_only=True)

    class Meta:
        model = DangerousCategory
        exclude = ('create_time', 'update_time')
        extra_kwargs = {
            'id': {'required': False}
        }

    def create(self, validated_data):
        """新建"""
        pk = uuid.uuid4()
        return DangerousCategory.objects.create(pk=pk, **validated_data)

    def update(self, instance, validated_data):
        """更新，instance为要更新的对象实例"""
        instance.name = validated_data.get('name', instance.name)
        instance.save()
        return instance