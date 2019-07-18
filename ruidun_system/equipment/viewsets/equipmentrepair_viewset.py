from lib.model_viewset import ModelViewSet
import django_filters as filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from ..models import EquipmentRepair
from ..serializers.equipmentrepair_serializer import EquipmentRepairSerializer

"""维修记录搜索查询"""
class EquipmentrepairFilter(filters.FilterSet):
    manager = filters.CharFilter(field_name="manager_id", lookup_expr="name")
    name = filters.CharFilter(field_name="equipment_id", lookup_expr="name")
    time_gt = filters.DateTimeFilter(field_name="time", lookup_expr='gte')
    time_lt = filters.DateTimeFilter(field_name="time", lookup_expr='lte')

    class Meta:
        model = EquipmentRepair
        fields = ["manager", 'equipment_id', "time_gt", "time_lt", "serviceman", "name"]

class EquipmentRepairViewSet(ModelViewSet):

    queryset = EquipmentRepair.objects.all()
    serializer_class = EquipmentRepairSerializer
    filterset_class = EquipmentrepairFilter
    filter_backends = [OrderingFilter, DjangoFilterBackend]
    ordering_fields = ("time",)

