import uuid
from staff.models import Staff
from rest_framework import serializers

from internet_setting.models import LocationCard
from staff.models import Staff
from staff.models import Company,Department


class LocationCardSerializer(serializers.ModelSerializer):
    staff_name = serializers.SerializerMethodField()



    class Meta:
        model = LocationCard
        fields = '__all__'
        extra_kwargs = {
            "id": {"read_only": True}
        }

    def get_staff_name(self, obj):
        return Staff.objects.filter(id=obj.card_id).values("name")

    # def validate_staff_id(self, value):
    #     if Staff.objects.filter(pk=value).count() == 0:
    #         raise serializers.ValidationError("无效的值，关联表中不存在这条记录")
    #     return value
    #
    # def get_department(self, obj):
    #     return obj.staff.department.name
    #
    # def get_company(self, obj):
    #     return obj.staff.company.name

    def create(self, validated_data):
        pk = uuid.uuid4()
        return LocationCard.objects.create(pk=pk, **validated_data)

    def update(self, instance, validated_data):
        instance.status = validated_data.get("status", instance.status)
        instance.card_id = validated_data.get("card_id", instance.card_id)
        instance.time = validated_data.get("time", instance.time)
        instance.save()
        return instance
