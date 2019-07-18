import uuid

from rest_framework import serializers

from auth_system.models import Part
from internet_setting.models import Voice, VoiceServer


class VoiceSerializer(serializers.ModelSerializer):
    part = serializers.SlugRelatedField(slug_field='name', read_only=True)
    server = serializers.SlugRelatedField(slug_field='name', read_only=True)
    part_id = serializers.CharField(allow_null=True, required=False)
    server_id = serializers.CharField(allow_null=True, required=False)

    class Meta:
        model = Voice
        fields = '__all__'
        extra_kwargs = {
            # "id": {"read_only": True},
        }

    def validate_part_id(self, value):
        if Part.objects.filter(pk=value).count() == 0:
            raise serializers.ValidationError("无效的值，关联表中不存在这条记录")
        return value

    def validate_server_id(self, value):
        if VoiceServer.objects.filter(pk=value).count() == 0:
            raise serializers.ValidationError("无效的值，关联表中不存在这条记录")
        return value

    def create(self, validated_data):
        # pk = uuid.uuid4()
        return Voice.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get("name", instance.name)
        instance.part_id = validated_data.get("part_id", instance.part_id)
        instance.server_id = validated_data.get("server_id", instance.server_id)
        instance.note = validated_data.get("note", instance.note)
        instance.is_used = validated_data.get("is_used", instance.is_used)
        instance.status = validated_data.get("status", instance.status)
        instance.factory = validated_data.get("factory", instance.factory)
        instance.model = validated_data.get("model", instance.model)
        instance.time = validated_data.get("time", instance.time)
        instance.x = validated_data.get("x", instance.x)
        instance.y = validated_data.get("y", instance.y)

        instance.save()
        return instance
