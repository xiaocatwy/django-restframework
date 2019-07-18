import uuid

from rest_framework import serializers
from auth_system.models import Project, Company

"""项目模型序列化"""
class ProjectSerializer(serializers.ModelSerializer):

    company = serializers.SlugRelatedField(label='单位', read_only=True, slug_field="name")
    company_id = serializers.CharField(allow_null=True,required=False)

    class Meta:
        model = Project
        fields = '__all__'
        extra_kwargs = {
            "id": {"required": False},
            "name": {"required": False}
        }
    #验证
    def validate_company_id(self, value):
        if Company.objects.filter(pk=value).count() == 0:
            raise serializers.ValidationError("无效的值")
        return value

    def create(self, validated_data):
        """新建"""
        validated_data['id'] = uuid.uuid4()
        return Project.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """更新，instance为要更新的对象实例"""
        instance.name = validated_data.get('name', instance.name)
        instance.index = validated_data.get('index', instance.index)
        instance.is_used = validated_data.get('is_used', instance.is_used)
        instance.company_id = validated_data.get('company_id', instance.company_id)
        instance.manager = validated_data.get('manager', instance.manager)
        instance.manager_phone = validated_data.get('manager_phone', instance.manager_phone)
        instance.save()
        return instance