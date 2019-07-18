import uuid

from rest_framework import serializers

from auth_system.models import Part
from internet_setting.models import DeviceInfo, DeviceCategory
from staff.models import Staff, Company
from equipment.models import Factory, Model


class DeviceInfoSerializer(serializers.ModelSerializer):

    # 指定外键同时显示id和name，name只序列化的时候使用，id为反序列化时使用，可以不用传
    # 如果外键仅仅是主键就不用下面的了
    # factory = serializers.SlugRelatedField(slug_field='name', read_only=True)
    # model = serializers.SlugRelatedField(slug_field='name', read_only=True)
    manager = serializers.SlugRelatedField(slug_field='name', read_only=True)
    company = serializers.SerializerMethodField()
    category = serializers.SlugRelatedField(slug_field='name', read_only=True)
    part = serializers.SlugRelatedField(slug_field='name', read_only=True)
    # factory_id = serializers.CharField(allow_null=True, required=False)
    # model_id = serializers.CharField(allow_null=True, required=False)
    manager_id = serializers.CharField(allow_null=True, required=False)
    part_id = serializers.CharField(allow_null=True, required=False)
    category_id = serializers.CharField(allow_null=True, required=False)

    class Meta:
        model = DeviceInfo
        fields = "__all__"
        extra_kwargs = {
            "id": {"read_only": True}  # 主键系统生成，不需要传
        }

    # 关于外键的需要单独验证,因为外键字段指定两个序列化字段会出现问题
    def validate_manager_id(self, value):
        if Staff.objects.filter(pk=value).count() == 0:
            raise serializers.ValidationError("无效的值，关联表中不存在这条记录")
        return value

    # def validate_model_id(self, value):
    #     if Model.objects.filter(pk=value).count() == 0:
    #         raise serializers.ValidationError("无效的值，关联表中不存在这条记录")
    #     return value
    #
    # def validate_factory_id(self, value):
    #     if Factory.objects.filter(pk=value).count() == 0:
    #         raise serializers.ValidationError("无效的值，关联表中不存在这条记录")
    #     return value

    def get_company(self, obj):
        return obj.part.company.name

    def validate_part_id(self, value):
        if Part.objects.filter(pk=value).count() == 0:
            raise serializers.ValidationError("无效的值，关联表中不存在这条记录")
        return value

    def validate_category_id(self, value):
        if DeviceCategory.objects.filter(pk=value).count() == 0:
            raise serializers.ValidationError("无效的值，关联表中不存在这条记录")
        return value

    def create(self, validated_data):
        validated_data["id"] = uuid.uuid4()  # 添加一个唯一的UUID为主键
        return DeviceInfo.objects.create(**validated_data)

    def update(self, instance, validated_data):
        # 因为有可能没有传过来，所以用字典.get() 方法
        instance.name = validated_data.get("name", instance.name)
        instance.time = validated_data.get("time", instance.time)
        instance.location = validated_data.get("location", instance.location)
        instance.factory = validated_data.get("factory", instance.factory)
        instance.model= validated_data.get("model", instance.model)
        instance.manager_id = validated_data.get("phone", instance.manager_id)
        instance.company_id = validated_data.get("company_id", instance.company_id)
        instance.category_id = validated_data.get("category_id", instance.category_id)
        instance.is_used = validated_data.get("is_used", instance.is_used)
        instance.index = validated_data.get("index", instance.index)
        instance.status = validated_data.get("status", instance.status)
        instance.note = validated_data.get("note", instance.note)
        instance.x = validated_data.get("x", instance.x)
        instance.y = validated_data.get("y", instance.y)

        instance.save()
        return instance


