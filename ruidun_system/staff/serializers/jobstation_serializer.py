import uuid

from rest_framework import serializers
from staff.models import JobStation


class JobStationSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobStation
        fields = '__all__'
        extra_kwargs = {
            "id": {"required": False}
        }

    def create(self, validated_data):
        """新建"""
        validated_data['id'] = uuid.uuid4()
        return JobStation.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """更新，instance为要更新的对象实例"""
        instance.name = validated_data.get('name', instance.name)
        instance.index = validated_data.get('index', instance.index)
        instance.is_used = validated_data.get('is_used', instance.is_used)
        instance.save()
        return instance