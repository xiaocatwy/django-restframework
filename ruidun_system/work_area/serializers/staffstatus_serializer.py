from rest_framework import serializers
from staff.models import Part, Team, Staff, Department


# class TeamSerializer(serializers.ModelSerializer):
#     """班组序列化器"""
#
#     class Meta:
#         model = Team
#         fields = ('name',)


class StaffSerializer(serializers.ModelSerializer):
    """工区人员状态序列化器"""

    # job_station
    # group_number_id = serializers.CharField(label='班组id', allow_null=True)
    # job_station = serializers.SlugRelatedField(label='工作岗位', read_only=True, slug_field='name')
    department = serializers.SerializerMethodField()

    class Meta:
        model = Staff
        fields = ('id', 'name', 'phone', 'department', 'medical_history')

    def get_department(self, obj):
        department_id = obj.department_id
        department = Department.objects.get(id=department_id)
        return department.department + '/' + department.group_name

