from rest_framework import serializers

from staff.models import Staff
from ..models import EquipmentLocation, EquipmentUsed


class EquipmentLocationSerializer(serializers.ModelSerializer):
    """工程车辆定位记录序列化器(暂时只有查询)"""
    # location_card_id = serializers.CharField(allow_null=True, required=False)
    equipment_name = serializers.SerializerMethodField()
    company_name = serializers.SerializerMethodField()
    model_name = serializers.SerializerMethodField()
    user_name = serializers.SerializerMethodField()

    class Meta:
        model = EquipmentLocation
        fields = "__all__"
        extra_kwargs = {
            "id": {"required": False}
        }

    def get_equipment_name(self, obj):
        return obj.location_card.equipment.name

    def get_company_name(self, obj):
        return obj.location_card.equipment.company.name

    def get_model_name(self, obj):
        return obj.location_card.equipment.model.name

    def get_user_name(self, obj):
        user_id = EquipmentUsed.objects.get(id=obj.location_card.equipment_id).user_id
        return Staff.objects.get(id=user_id).name







