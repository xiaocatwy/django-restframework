import uuid

from rest_framework import serializers
from ..models import SpecialScheme, Method


class MethodSerializer(serializers.ModelSerializer):
    """应急演练序列化器"""

    class Meta:
        model = Method
        fields = '__all__'
        extra_kwargs = {
            'id': {'read_only': True},
        }

    def create(self, validated_data):
        """新建"""
        pk = uuid.uuid4()

        people = self.context["request"].user.staff.name if self.context["request"].user.staff else "匿名用户"
        return Method.objects.create(pk=pk,people=people, **validated_data)

    def update(self, instance, validated_data):
        """更新，instance为要更新的对象实例"""
        instance.name = validated_data.get('name', instance.name)
        instance.people = validated_data.get('people', instance.people)
        instance.phone = validated_data.get('phone', instance.phone)
        instance.time = validated_data.get('time', instance.time)
        instance.use_message = validated_data.get('use_message', instance.use_message)
        instance.message_content = validated_data.get('message_content', instance.message_content)
        instance.set_light = validated_data.get('set_light', instance.set_light)
        instance.set_ling = validated_data.get('set_ling', instance.set_ling)
        instance.set_voice = validated_data.get(''
                                                'set_voice', instance.set_voice)
        instance.save()
        return instance