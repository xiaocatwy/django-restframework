import uuid

from rest_framework import serializers
from staff.models import Team

"""施工组序列化"""
class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = '__all__'
        extra_kwargs = {
            "id": {"required": False},
            "name": {"required": False}
        }

    def create(self, validated_data):
        """新建"""
        validated_data['id'] = uuid.uuid4()
        return Team.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """更新，instance为要更新的对象实例"""

        instance.name = validated_data.get('name', instance.name)
        instance.index = validated_data.get('index', instance.index)
        instance.is_used = validated_data.get('is_used', instance.is_used)
        instance.save()
        return instance