import uuid

from rest_framework import serializers
from ..models import StaffBreak


class StaffBreakSerializer(serializers.ModelSerializer):
    """人员道闸序列化器"""

    class Meta:
        model = StaffBreak
        fields = '__all__'
        extra_kwargs = {
            'id': {'required': False}
        }

    def create(self, validated_data):
        """新建"""
        pk = uuid.uuid4()
        return StaffBreak.objects.create(pk=pk, **validated_data)

    def update(self, instance, validated_data):
        """更新，instance为要更新的对象实例"""
        instance.id = validated_data.get('id', instance.id)
        instance.part_id = validated_data.get('part_id', instance.part_id)
        instance.name = validated_data.get('name', instance.name)
        instance.save()
        return instance