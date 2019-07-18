import uuid

from rest_framework import serializers

from auth_system.models import Part
from internet_setting.models import LEDInfo


class LEDInfoSerializer(serializers.ModelSerializer):

    part = serializers.SlugRelatedField(slug_field='name', read_only=True)
    part_id = serializers.CharField(allow_null=True, required=False)

    class Meta:
        model = LEDInfo
        fields = "__all__"
        extra_kwargs = {
            "id":{"read_only": True},
            "sysid":{"read_only": True},
            "part_id":{"read_only": True},
            "note":{"required": False},
            "area_name":{"required": False}
        }

    # 关于外键的需要单独验证,因为外键字段指定两个序列化字段会出现问题

    def validate_part_id(self, value):
        if Part.objects.filter(pk=value).count() == 0:
            raise serializers.ValidationError("无效的值，关联表中不存在这条记录")
        return value

    def create(self, validated_data):
        validated_data["id"] = uuid.uuid4()  # 添加一个唯一的UUID为主键
        return LEDInfo.objects.create(**validated_data)

    def update(self, instance, validated_data):
        # 因为有可能没有传过来，所以用字典.get() 方法
        instance.time = validated_data.get("time", instance.bought_time)
        instance.factory = validated_data.get("factory", instance.factory)
        instance.model= validated_data.get("model", instance.model)
        instance.ip = validated_data.get("ip", instance.ip)
        instance.port = validated_data.get("port", instance.port)
        instance.part_id = validated_data.get("part_id", instance.part_id)
        instance.is_used = validated_data.get("is_used", instance.is_used)
        instance.status = validated_data.get("status", instance.status)
        instance.note = validated_data.get("note", instance.note)
        instance.x = validated_data.get("x", instance.x)
        instance.y = validated_data.get("y", instance.y)
        instance.sysid = validated_data.get("sysid", instance.sysid)
        instance.area_name = validated_data.get("area_name", instance.area_name)
        instance.nScreenNo = validated_data.get("nScreenNo", instance.nScreenNo)
        instance.pScreenName = validated_data.get("pScreenName", instance.pScreenName)
        instance.nWidth = validated_data.get("nWidth", instance.nWidth)
        instance.nHeight = validated_data.get("nHeight", instance.nHeight)
        instance.nScreenType = validated_data.get("nScreenType", instance.nScreenType)
        instance.nPixelMode = validated_data.get("nPixelMode", instance.nPixelMode)

        instance.save()
        return instance


