import uuid

from rest_framework import serializers

from internet_setting.models import DeviceCategory


class DeviceCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = DeviceCategory
        fields = '__all__'
        extra_kwargs = {
            "id": {"read_only": True},
        }

    def create(self, validated_data):
        pk = uuid.uuid4()
        return DeviceCategory.objects.create(pk=pk, **validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get("name", instance.name)
        instance.index = validated_data.get("index", instance.index)
        instance.is_used = validated_data.get("is_used", instance.is_used)

        instance.save()
        return instance
