import uuid

from rest_framework import serializers

from auth_system.models import Part
from internet_setting.models import Voice, VoiceServer, IPSwitch, IPSwitchDetail


class IPSwitchDetailSerializer(serializers.ModelSerializer):
    part = serializers.SlugRelatedField(slug_field='name', read_only=True)
    part_id = serializers.CharField(allow_null=True, required=False)
    ipswitch = serializers.SlugRelatedField(slug_field='name', read_only=True)
    ipswitch_id = serializers.CharField(allow_null=True, required=False)

    class Meta:
        model = IPSwitchDetail
        fields = '__all__'
        extra_kwargs = {
            "id": {"read_only": True},
        }

    def validate_part_id(self, value):
        if Part.objects.filter(pk=value).count() == 0:
            raise serializers.ValidationError("无效的值，关联表中不存在这条记录")
        return value

    def validate_ipswitch_id(self, value):
        if IPSwitch.objects.filter(pk=value).count() == 0:
            raise serializers.ValidationError("无效的值，关联表中不存在这条记录")
        return value

    def create(self, validated_data):
        pk = uuid.uuid4()
        return IPSwitchDetail.objects.create(pk=pk, **validated_data)

    def update(self, instance, validated_data):
        instance.number = validated_data.get("part_id", instance.part_id)
        instance.ipswitch_id = validated_data.get("server_id", instance.server_id)
        instance.content = validated_data.get("note", instance.note)
        instance.note = validated_data.get("is_used", instance.is_used)
        instance.part_id = validated_data.get("status", instance.status)

        instance.save()
        return instance
