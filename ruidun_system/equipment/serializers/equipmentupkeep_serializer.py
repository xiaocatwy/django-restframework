import time
import uuid

from rest_framework import serializers

from staff.models import Staff
from ..models import EquipmentUpkeep, EquipmentInfo
from equipment.serializers.equipmentinfo_serializer import EquipmentinfopSerializer

class EquipmentUpkeepSerializer(serializers.ModelSerializer):
    """工程车辆保养记录序列化器"""
    equipment = EquipmentinfopSerializer(read_only=True)
    manager = serializers.SlugRelatedField(read_only=True, slug_field="name")
    manager_id = serializers.CharField(allow_null=True, required=False)
    equipment_id = serializers.CharField(allow_null=True, required=False)
    car_age = serializers.SerializerMethodField()

    class Meta:
        model = EquipmentUpkeep
        fields = '__all__'
        extra_kwargs = {
            "id": {"required": False}
        }

    def get_car_age(self, obj):
        a = int(str(obj.equipment.bought_time)[0:4])
        b = int(time.strftime("%Y"))
        return b-a+1

    def validate_equipment_id(self, value):
        if EquipmentInfo.objects.filter(pk=value).count() == 0:
            raise serializers.ValidationError("无效的值")
        return value

    def validate_manager_id(self, value):
        if Staff.objects.filter(pk=value).count() == 0:
            raise serializers.ValidationError("无效的值")
        return value

    def create(self, validated_data):
        """新建"""
        validated_data['id'] = uuid.uuid4()
        return EquipmentUpkeep.objects.create(**validated_data)