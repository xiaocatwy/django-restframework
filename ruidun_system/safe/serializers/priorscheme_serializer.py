import uuid

from rest_framework import serializers
from ..models import PriorScheme


class PriorSchemeSerializer(serializers.ModelSerializer):
    """应急方案序列化器"""

    staff_id = serializers.CharField(label='上传者id')
    staff = serializers.SlugRelatedField(label='员工', read_only=True, slug_field='name')

    class Meta:
        model = PriorScheme
        fields = '__all__'
        extra_kwargs = {
            'id': {'read_only': True},
            'path': {'required': False},
            'download_times': {'required': False}
        }

    def create(self, validated_data):
        """新建"""
        pk = uuid.uuid4()

        # 没有上传文件抛出错误(考虑到更新时不需要传入文件)
        request = self.context['request']
        if not request.data.get('path'):
            raise serializers.ValidationError('没有上传文件')

        return PriorScheme.objects.create(pk=pk, **validated_data)

    def update(self, instance, validated_data):
        """更新，instance为要更新的对象实例"""
        instance.staff_id = validated_data.get('staff_id', instance.staff_id)
        instance.name = validated_data.get('name', instance.name)
        instance.path = validated_data.get('path', instance.path)
        instance.download_times = validated_data.get('download_times', instance.download_times)
        instance.reate_time = validated_data.get('reate_time', instance.reate_time)
        instance.update_time = validated_data.get('update_time', instance.update_time)
        instance.save()
        return instance
