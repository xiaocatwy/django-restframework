import uuid

from rest_framework import serializers

from staff.models import Folk, Staff


class FolkSerializer(serializers.ModelSerializer):
    staff = serializers.SlugRelatedField(read_only=True, slug_field="name")
    staff_id = serializers.CharField(allow_null=True, required=False)

    class Meta:
        model = Folk
        fields = '__all__'
        extra_kwargs = {
            "id": {"required": False},
            "name": {"required": False}
        }

    # 验证
    def validate_staff_id(self, value):
        if Staff.objects.filter(pk=value).count() == 0:
            raise serializers.ValidationError("无效的值")
        return value

    def create(self, validated_data):
        """新建"""
        validated_data['id'] = uuid.uuid4()
        return Folk.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """更新，instance为要更新的对象实例"""
        instance.name = validated_data.get('name', instance.name)
        instance.phone = validated_data.get('phone', instance.phone)
        instance.address = validated_data.get('address', instance.address)
        instance.staff_id = validated_data.get('staff_id', instance.staff_id)
        instance.save()
        return instance