import uuid

from rest_framework import serializers
from ..models import CarBreak


class CarBreakSerializer(serializers.ModelSerializer):
    """车辆道闸序列化器"""

    part = serializers.SlugRelatedField(slug_field='name', read_only=True)
    part_id = serializers.CharField(allow_null=True)

    class Meta:
        model = CarBreak
        fields = '__all__'
        extra_kwargs = {
            'id': {'required': False}
        }

    def create(self, validated_data):
        """新建"""
        pk = uuid.uuid4()
        return CarBreak.objects.create(pk=pk, **validated_data)

    def update(self, instance, validated_data):
        """更新，instance为要更新的对象实例"""
        instance.id = validated_data.get('id', instance.id)
        instance.part_id = validated_data.get('part_id', instance.part_id)
        instance.name = validated_data.get('name', instance.name)
        instance.x = validated_data.get('x', instance.x)
        instance.y = validated_data.get('y', instance.y)
        instance.save()
        return instance
