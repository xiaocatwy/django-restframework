import uuid

from rest_framework import serializers

from internet_setting.models import DeviceUpkeep, DeviceInfo
from staff.models import Staff


class DeviceUpkeepSerializer(serializers.ModelSerializer):
    manager = serializers.SlugRelatedField(slug_field='name', read_only=True)
    manager_id = serializers.CharField(allow_null=True, required=False)
    device = serializers.SlugRelatedField(slug_field='name', read_only=True)
    device_id = serializers.CharField(allow_null=True, required=False)

    class Meta:
        model = DeviceUpkeep
        fields = '__all__'
        extra_kwargs = {
            "id": {"read_only": True}
        }

    def validate_manager_id(self, value):
        if Staff.objects.filter(pk=value).count() == 0:
            raise serializers.ValidationError("无效的值，关联表中不存在这条记录")
        return value

    def validate_device_id(self, value):
        if DeviceInfo.objects.filter(pk=value).count() == 0:
            raise serializers.ValidationError("无效的值，关联表中不存在这条记录")
        return value

    def create(self, validated_data):
        pk = uuid.uuid4()
        return DeviceUpkeep.objects.create(pk=pk, **validated_data)

    def update(self, instance, validated_data):
        instance.manager_id = validated_data.get("manager_id", instance.manager_id)
        instance.device_id = validated_data.get("device_id", instance.device_id)
        instance.upkeep_man = validated_data.get("upkeep_man", instance.upkeep_man)
        instance.time = validated_data.get("time", instance.time)

        instance.save()
        return instance