from rest_framework import serializers
from staff.models import Department


class DepartmentSerializer(serializers.ModelSerializer):
    """班组序列化器"""
    # staff_set = serializers.PrimaryKeyRelatedField(read_only=True, many=True)
    department = serializers.SerializerMethodField()

    class Meta:
        model = Department
        fields = ('id', 'department')

    def get_department(self, obj):

        return obj.department + '/' + obj.group_name