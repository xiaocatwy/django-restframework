# import uuid
#
# from rest_framework import serializers
# from staff.models import Department
#
#
# class DepartmentSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Department
#         fields = '__all__'
#         extra_kwargs = {
#             "id": {"required": False}
#         }
#
#     def create(self, validated_data):
#         """新建"""
#         validated_data['id'] = uuid.uuid4()
#         return Department.objects.create(**validated_data)
#
#     def update(self, instance, validated_data):
#         """更新，instance为要更新的对象实例"""
#         instance.department = validated_data.get('department', instance.department)
#         instance.group_name = validated_data.get('group_name', instance.group_name)
#
#         instance.save()
#         return instance


import uuid
from random import random

from rest_framework import serializers
from staff.models import Department, Staff


class DepartmentSerializer(serializers.ModelSerializer):
    part = serializers.SlugRelatedField(slug_field='name', read_only=True)
    part_id = serializers.CharField(allow_null=True, required=False)
    department_group = serializers.SerializerMethodField()
    staff_id = serializers.CharField(allow_null=True, required=False)
    staff_name = serializers.SerializerMethodField()

    class Meta:
        model = Department
        fields = '__all__'
        extra_kwargs = {
            "id": {"required": False},
            "group_name": {"required": False},
            "sysid": {"required": False}
        }

    def get_department_group(self, obj):

        return obj.department+"/"+obj.group_name

    def get_staff_name(self, obj):

        try:
            staff = Staff.objects.get(id=obj.staff_id)
        except Exception:
            return None

        return staff.name

    def create(self, validated_data):
        """新建"""
        a = Department.objects.latest('id')
        id = a.id + 1
        return Department.objects.create(pk=id, **validated_data)

    def update(self, instance, validated_data):
        """更新，instance为要更新的对象实例"""
        instance.department = validated_data.get('department', instance.department)
        instance.group_name = validated_data.get('group_name', instance.group_name)
        instance.remarks = validated_data.get('remarks', instance.remarks)
        instance.part_id = validated_data.get("part_id", instance.part_id)
        instance.staff_id = validated_data.get("staff_id", instance.staff_id)
        instance.status = validated_data.get("status", instance.status)
        instance.save()
        return instance