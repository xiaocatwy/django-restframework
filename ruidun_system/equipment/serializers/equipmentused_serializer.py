import uuid

from rest_framework import serializers

from equipment.serializers.equipmentinfo_serializer import EquipmentinfosSerializer

from ..models import EquipmentUsed, EquipmentInfo
from staff.models import Staff
class EquipmentUsedSerializer(serializers.ModelSerializer):
    """工程车辆使用记录序列化器"""
    equipment = EquipmentinfosSerializer(read_only=True)
    manager = serializers.SlugRelatedField(label='负责人', read_only=True, slug_field="name")
    user = serializers.SlugRelatedField(label='使用人', read_only=True, slug_field="name")
    manager_id = serializers.CharField(allow_null=True, required=False)
    user_id = serializers.CharField(allow_null=True, required=False)
    equipment_id = serializers.CharField(allow_null=True, required=False)

    class Meta:
        model = EquipmentUsed
        fields = '__all__'
        extra_kwargs = {
            "id": {"required": False},
        }

    def validate_manager_id(self, value):
        if Staff.objects.filter(pk=value).count() == 0:
            raise serializers.ValidationError("无效的值")
        return value

    def validate_user_id(self, value):
        if Staff.objects.filter(pk=value).count() == 0:
            raise serializers.ValidationError("无效的值")
        return value

    def validate_equipment_id(self, value):
        if EquipmentInfo.objects.filter(pk=value).count() == 0:
            raise serializers.ValidationError("无效的值")
        return value

    def create(self, validated_data):
        """新建"""
        validated_data['id'] = uuid.uuid4()
        return EquipmentUsed.objects.create(**validated_data)