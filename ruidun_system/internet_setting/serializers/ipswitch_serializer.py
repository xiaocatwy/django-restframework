import uuid

from rest_framework import serializers

from auth_system.models import Part
from internet_setting.models import VoiceServer, IPSwitch
from internet_setting.serializers.ipswitch_detail_serializer import IPSwitchDetailSerializer


class IPSwitchSerializer(serializers.ModelSerializer):
    part = serializers.SlugRelatedField(slug_field='name', read_only=True)
    part_id = serializers.CharField(allow_null=True, required=False)
    detail = serializers.SerializerMethodField()

    class Meta:
        model = IPSwitch
        fields = '__all__'
        extra_kwargs = {
            "id": {"read_only": True},
        }

    def get_detail(self, obj):
        return IPSwitchDetailSerializer(obj.detail.all(), many=True).data

    def validate_part_id(self, value):
        if Part.objects.filter(pk=value).count() == 0:
            raise serializers.ValidationError("无效的值，关联表中不存在这条记录")
        return value

    def create(self, validated_data):
        pk = uuid.uuid4()
        return IPSwitch.objects.create(pk=pk, **validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get("name", instance.name)
        instance.ip = validated_data.get("ip", instance.ip)
        instance.part_id = validated_data.get("part_id", instance.part_id)
        instance.port = validated_data.get("port", instance.port)
        instance.note = validated_data.get("note", instance.note)
        instance.x = validated_data.get("x", instance.x)
        instance.y = validated_data.get("y", instance.y)
        # instance.is_used = validated_data.get("is_used", instance.is_used)

        instance.save()
        return instance
