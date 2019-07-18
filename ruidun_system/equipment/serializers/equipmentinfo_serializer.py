import uuid
import time
from rest_framework import serializers

from ..models import EquipmentInfo, Company


class EquipmentInfoSerializer(serializers.ModelSerializer):
    """工程车辆基础信息序列化器1"""

    company = serializers.SlugRelatedField(label='单位', read_only=True, slug_field="name")
    company_id = serializers.CharField(allow_null=True, required=False)
    part = serializers.SlugRelatedField(label='工区', read_only=True, slug_field="name")
    part_id = serializers.CharField(allow_null=True, required=False)
    car_age = serializers.SerializerMethodField()

    class Meta:
        model = EquipmentInfo
        exclude = ('mileage',)
        extra_kwargs = {
            "id": {"required": False},
            "name": {"required": False},
            "mileage": {"required": False},
            "bought_time": {"required": False},
            # "factory": {"allow_null": True, "required": False},
            # "model": {"allow_null": True, "required": False}
        }

    def get_car_age(self, obj):
        a = int(str(obj.bought_time)[0:4])
        b = int(time.strftime("%Y"))
        return b-a

    #外键验证
    def validate_company_id(self, value):
        if Company.objects.filter(pk=value).count() == 0:
            raise serializers.ValidationError("无效的值")
        return value



    def create(self, validated_data):
        """新建"""
        validated_data['id'] = uuid.uuid4()
        return EquipmentInfo.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """更新，instance为要更新的对象实例"""
        instance.name = validated_data.get('name', instance.name)
        instance.bought_time = validated_data.get('bought_time', instance.bought_time)
        instance.is_used = validated_data.get('is_used', instance.is_used)
        instance.mileage = validated_data.get('mileage', instance.mileage)
        instance.company_id = validated_data.get('company_id', instance.company_id)
        instance.part_id = validated_data.get('part_id', instance.part_id)
        instance.factory = validated_data.get('factory', instance.factory)
        instance.model = validated_data.get('model', instance.model)
        instance.save()
        return instance


"""工程车辆基础信息序列化器2"""
class EquipmentinfosSerializer(serializers.ModelSerializer):
    company = serializers.SlugRelatedField(label='单位', read_only=True, slug_field="name")

    class Meta:
        model = EquipmentInfo
        fields = ('name', 'company', 'model', 'mileage')


"""工程车辆基础信息序列化器3"""
class EquipmentinfopSerializer(serializers.ModelSerializer):
    company = serializers.SlugRelatedField(label='单位', read_only=True, slug_field="name")

    class Meta:
        model = EquipmentInfo
        fields = ('name', 'company', 'factory', 'model', 'company_id')


"""工程车辆基础信息序列化器4"""
class EquipmentinfolSerializer(serializers.ModelSerializer):
    company = serializers.SlugRelatedField(label='单位', read_only=True, slug_field="name")

    class Meta:
        model = EquipmentInfo
        fields = ('name', 'company', 'model')