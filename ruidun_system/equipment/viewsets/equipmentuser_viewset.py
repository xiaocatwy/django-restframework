import django_filters as filters
from lib.model_viewset import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from ..models import EquipmentUsed
from ..serializers.equipmentused_serializer import EquipmentUsedSerializer

"""使用记录搜索查询"""
class EquipmentuserFilter(filters.FilterSet):
    time_gt = filters.DateTimeFilter(field_name="start_time", lookup_expr='gte')
    time_lt = filters.DateTimeFilter(field_name="start_time", lookup_expr='lte')
    user_name = filters.CharFilter(field_name="user_id", lookup_expr='name')
    equipment_name = filters.CharFilter(field_name="equipment_id", lookup_expr="name")
    manager_name = filters.CharFilter(field_name="manager_id", lookup_expr="name")

    class Meta:
        model = EquipmentUsed
        fields = ["time_gt", "time_lt", 'user_name', "equipment_id", "manager_name", "equipment_name"]


class EquipmentUsedViewSet(ModelViewSet):
    queryset = EquipmentUsed.objects.all()
    serializer_class = EquipmentUsedSerializer
    filterset_class = EquipmentuserFilter
    filter_backends = [OrderingFilter, DjangoFilterBackend]
    ordering_fields = ("start_time", "id")


