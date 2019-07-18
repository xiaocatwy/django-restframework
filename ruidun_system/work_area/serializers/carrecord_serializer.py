from rest_framework import serializers

from internet_setting.models import CarPass
from ..models import CarRecord, CarInfo, CarBreak


class CarInfoSerializer(serializers.ModelSerializer):
    """车辆信息序列化器"""

    code = serializers.SerializerMethodField()

    class Meta:
        model = CarInfo
        fields = ('code', 'id', 'car_owner', 'phone_number')

    def get_code(self, obj):
        request = self.context['request']
        part_id = request.query_params.get('part_id')
        # TODO 等待传入part_id
        carpass_set = obj.carpass_set.filter(part_id=1)
        # return map(lambda p: {"code": p.code}, staffpass_set)

        if not carpass_set:
            return None

        return (carpass_set[0].code)


class CarRecordSerializer(serializers.ModelSerializer):
    """车辆通行记录序列化器"""

    # car = CarInfoSerializer(read_only=True)
    # car_break = serializers.SlugRelatedField(label='道闸', read_only=True, slug_field='name')

    class Meta:
        model = CarRecord
        # fields = ('id', 'car', 'car_break', 'in_out', 'time')
        fields = ('id', 'cardid', 'cardnumber', 'intime', 'inplace', 'outtime', 'outplace')


