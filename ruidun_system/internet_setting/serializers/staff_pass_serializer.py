import uuid

from rest_framework import serializers

from internet_setting.models import StaffPass
from staff.models import Staff


class StaffPassSerializer(serializers.ModelSerializer):

    staff = serializers.SlugRelatedField(slug_field='name', read_only=True)
    staff_id = serializers.CharField(allow_null=True, required=False)

    class Meta:
        model = StaffPass
        fields = '__all__'
        extra_kwargs = {
            "id": {"read_only": True}
        }

    def validate_staff_id(self, value):
        if Staff.objects.filter(pk=value).count() == 0:
            raise serializers.ValidationError("无效的值，关联表中不存在这条记录")
        return value

    def create(self, validated_data):
        pk = uuid.uuid4()
        return StaffPass.objects.create(pk=pk, **validated_data)

    def update(self, instance, validated_data):
        instance.status = validated_data.get("status", instance.status)
        instance.staff_id = validated_data.get("staff_id", instance.staff_id)
        instance.is_used = validated_data.get("is_used", instance.is_used)
        instance.code = validated_data.get("code", instance.code)

        instance.save()
        return instance