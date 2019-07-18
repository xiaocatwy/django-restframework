from ..models import StaffBreak
from ..serializers.staffbreak_serializer import StaffBreakSerializer
from lib.model_viewset import ModelViewSet


class StaffBreakViewset(ModelViewSet):
    """人员道闸"""

    queryset = StaffBreak.objects.filter(is_used=1)
    serializer_class = StaffBreakSerializer
    filter_fields = ('part_id',)