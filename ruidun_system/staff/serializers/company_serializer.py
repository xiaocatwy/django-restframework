from rest_framework import serializers

import uuid

from auth_system.models import Company


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'
        extra_kwargs = {
            "id": {"read_only":True},
            "boss_name": {"required": False},
            "phone_num": {"required": False},
            "name": {"required": False},
            "company_address": {"required": False}
        }

    def create(self, validated_data):
        """新建"""
        validated_data['id'] = uuid.uuid4()
        return Company.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """更新，instance为要更新的对象实例"""

        instance.name = validated_data.get('name', instance.name)
        instance.index = validated_data.get('index', instance.index)
        instance.is_used = validated_data.get('is_used', instance.is_used)
        instance.boss_name = validated_data.get('boss_name', instance.boss_name)
        instance.phone_num = validated_data.get('phone_num', instance.phone_num)
        instance.company_address = validated_data.get('company_address', instance.company_address)
        instance.save()
        return instance

