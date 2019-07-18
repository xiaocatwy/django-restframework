from rest_framework import serializers

from auth_system.models import Part
from internet_setting.models import StaffPass
from ..models import StaffBreak, StaffRecord
from staff.models import Staff


class StaffSerializer(serializers.ModelSerializer):
    """人员序列化器"""

    code = serializers.SerializerMethodField()
    # part = serializers.SerializerMethodField()

    class Meta:
        model = Staff
        fields = ('code', 'id', 'name', 'phone')

    def get_code(self, obj):
        # 人员通行证卡号
        request = self.context['request']
        part_id = request.query_params.get('part_id')
        # TODO 等待传入part_id(下方)
        staffpass_set = obj.staffpass_set.filter(part_id=1)

        if not staffpass_set:
            return None

        return (staffpass_set[0].code)

    # def get_part(self, obj):
    #     # 判断人员是否属于当前工区
    #     request = self.context['request']
    #     part_id = request.query_params.get('part_id')
    #     # TODO 等待传入part_id(下方)
    #
    #     if not part_id:
    #         raise serializers.ValidationError("参数不足")
    #
    #     if not Part.objects.filter(id=part_id):
    #         raise serializers.ValidationError("工区不存在")
    #
    #     if obj.part_id != part_id:
    #         # 判断人员是否属于当前工区
    #         part_name = Part.objects.filter(id=obj.part_id)[0].name
    #         return part_name


# class StaffBreakSerializer  (serializers.ModelSerializer):
#     """人员道闸序列化器"""
#
#     class Meta:
#         model = StaffBreak
#         fields = ('name',)
#         # extra_kwargs = {
#         #     'name': {'label': '道闸'}
#         # }


# class StffPassSerializer(serializers.ModelSerializer):
#     """人员通行证序列化器"""
#
#     class Meta:
#         model = StaffPass
#         fields = ('code', )


class StaffRecordSerializer(serializers.ModelSerializer):
    """人员通行记录序列化器"""

    # staff = StaffSerializer(read_only=True)
    # staff_break = serializers.SlugRelatedField(label='道闸', read_only=True, slug_field='name')

    class Meta:
        model = StaffRecord
        # fields = ('id', 'staff', 'staff_break', 'in_out', 'time')
        fields = ('id', 'sysid', 'zone_name', 'device_name', 'names', 'card_number', 'inouts', 'time', 'group_number')