from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
import django_filters as filters

from client.location import Client
from lib.model_viewset import ModelViewSet
from lib.user_permission import SelfPermission
from ..models import EquipmentLocation
from ..serializers.equipmentlocation_seriallizer import EquipmentLocationSerializer

# 查询设备的轨迹
class EquipmentLocationFilter(filters.FilterSet):
    time_gt = filters.DateTimeFilter(field_name="time", lookup_expr='gte')
    time_lt = filters.DateTimeFilter(field_name="time", lookup_expr='lte')
    equipment_name = filters.CharFilter(field_name="location_card_id", lookup_expr='equipment__name')
    user_name = filters.CharFilter(field_name="location_card_id", lookup_expr='equipment__equipmentused__user__name')

    class Meta:
        model = EquipmentLocation
        fields = ["time_gt", "time_lt", "location_card_id", "location", "user_name", "equipment_name"]


class EquipmentLocationViewSet(ModelViewSet):
    queryset = EquipmentLocation.objects.all()
    serializer_class = EquipmentLocationSerializer
    filterset_class = EquipmentLocationFilter
    filter_backends = [OrderingFilter, DjangoFilterBackend]
    ordering_fields = ("time", "id")


