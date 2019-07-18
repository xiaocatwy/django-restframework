import uuid

from rest_framework import serializers
from auth_system.models import User_Department


class UserDepartementSerializer(serializers.ModelSerializer):
    class Meta:
        model = User_Department
        fields = '__all__'
        extra_kwargs = {
            "id": {"required": False},
            "name": {"required": False}
        }

    def create(self, validated_data):
        """新建"""
        return User_Department.objects.create(pk=uuid.uuid4(), **validated_data)

    def update(self, instance, validated_data):
        """更新，instance为要更新的对象实例"""

        instance.name = validated_data.get('name', instance.name)
        instance.index = validated_data.get('index', instance.index)
        instance.is_used = validated_data.get('is_used', instance.is_used)
        instance.save()
        return instance