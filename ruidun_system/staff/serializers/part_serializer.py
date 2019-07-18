import uuid

from rest_framework import serializers
from auth_system.models import Project, Part

"""工区模型序列化"""


class PartSerializer(serializers.ModelSerializer):
    project = serializers.SlugRelatedField(read_only=True, slug_field="name")
    project_id = serializers.CharField(allow_null=True, required=False)
    company = serializers.SerializerMethodField()
    company_id = serializers.SerializerMethodField()
    class Meta:
        model = Part
        fields = '__all__'
        extra_kwargs = {
            "id": {"required": False},
            "name": {"required": False},
            "sysid":{"required": False}
        }

    def get_company(self, obj):
        return obj.project.company.name

    def get_company_id(self, obj):
        return obj.project.company.id

    # 验证
    def validate_project_id(self, value):
        if Project.objects.filter(pk=value).count() == 0:
            raise serializers.ValidationError("无效的值")
        return value

    def create(self, validated_data):
        """新建"""
        validated_data['id'] = uuid.uuid4()
        return Part.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """更新，instance为要更新的对象实例"""
        instance.name = validated_data.get('name', instance.name)
        instance.index = validated_data.get('index', instance.index)
        instance.is_used = validated_data.get('is_used', instance.is_used)
        instance.project_id = validated_data.get('project_id', instance.project_id)
        instance.manager = validated_data.get('manager', instance.manager)
        instance.manager_phone = validated_data.get('manager_phone', instance.manager_phone)
        instance.save()
        return instance