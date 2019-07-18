from rest_framework.response import Response

from ..models import CarBreak
from ..serializers.carbreak_serializer import CarBreakSerializer
from lib.model_viewset import ModelViewSet


class CarBreakViewset(ModelViewSet):
    """车辆道闸

    get:
    获取全部道闸信息

    """
    queryset = CarBreak.objects.filter(is_used=1)
    serializer_class = CarBreakSerializer
    filter_fields = ('part_id', )