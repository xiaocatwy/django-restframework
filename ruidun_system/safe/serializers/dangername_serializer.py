import uuid

from rest_framework import serializers
from safe.models import Danger


class DangerNameSerializer(serializers.ModelSerializer):
    """危险品名字序列化器（搜索字段）"""
    part_id = serializers.CharField(allow_null=True, required=False)
    part = serializers.SlugRelatedField(slug_field='name', read_only=True)
    category_id = serializers.CharField(allow_null=True, required=False)
    category =  serializers.SlugRelatedField(slug_field='name', read_only=True)
    class Meta:
        model = Danger
        fields = '__all__'
            #('id', 'name')
        extra_kwargs = {
            'id': {'read_only': True},
        }

    def create(self, validated_data):
        """新建"""
        pk = uuid.uuid4()
        # print(validated_data)
        return Danger.objects.create(pk=pk, **validated_data)

    def update(self, instance, validated_data):
        """更新，instance为要更新的对象实例"""
        instance.category_id = validated_data.get('category_id', instance.category_id)
        instance.part_id = validated_data.get('part_id', instance.part_id)
        instance.count = validated_data.get('count', instance.count)
        instance.name = validated_data.get('name', instance.name)
        instance.save()
        return instance