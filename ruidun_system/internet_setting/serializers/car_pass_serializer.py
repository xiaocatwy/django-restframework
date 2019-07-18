import uuid

from rest_framework import serializers

from internet_setting.models import CarPass


# class CarPassSerializer(serializers.ModelSerializer):
#
#     name = serializers.SerializerMethodField()
#
#     class Meta:
#         model = CarPass
#         fields = '__all__'
#         extra_kwargs = {
#             "id": {"read_only": True}
#         }
#
#     def get_name(self, obj):
#         return obj.car.car_owner
#
#     def create(self, validated_data):
#         pk = uuid.uuid4()
#         return CarPass.objects.create(pk=pk, **validated_data)
#
#     def update(self, instance, validated_data):
#         instance.status = validated_data.get("status", instance.status)
#         instance.car = validated_data.get("car", instance.car)
#         instance.is_used = validated_data.get("is_used", instance.is_used)
#         instance.code = validated_data.get("code", instance.code)
#
#         instance.save()
#         return instance
from work_area.models import CarInfo


class CarPassSerializer(serializers.ModelSerializer):

    part = serializers.SlugRelatedField(slug_field='name', read_only=True)
    part_id = serializers.CharField(allow_null=True)

    class Meta:
        model = CarInfo
        fields = '__all__'
        extra_kwargs = {
            "id": {"read_only": True}
        }


    def create(self, validated_data):
        pk = uuid.uuid4()
        return CarInfo.objects.create(pk=pk, **validated_data)

    # def update(self, instance, validated_data):
    #     instance.status = validated_data.get("status", instance.status)
    #     instance.car = validated_data.get("car", instance.car)
    #     instance.is_used = validated_data.get("is_used", instance.is_used)
    #     instance.code = validated_data.get("code", instance.code)
    #
    #     instance.save()
    #     return instance

    def update(self, instance, validated_data):
        instance.cphm = validated_data.get("cphm", instance.cphm)
        instance.clys = validated_data.get("clys", instance.clys)
        instance.clxh = validated_data.get("clxh", instance.clxh)
        instance.part_id = validated_data.get("part_id", instance.part_id)

        instance.save()
        return instance