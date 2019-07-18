from lib.model_viewset import ModelViewSet
import django_filters as filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from ..models import EquipmentUpkeep
from ..serializers.equipmentupkeep_serializer import EquipmentUpkeepSerializer


class EquipmentupkeepFilter(filters.FilterSet):
    manager_name = filters.CharFilter(field_name="manager_id", lookup_expr="name")
    name = filters.CharFilter(field_name="equipment_id", lookup_expr="name")
    time_gt = filters.DateTimeFilter(field_name="time", lookup_expr='gte')
    time_lt = filters.DateTimeFilter(field_name="time", lookup_expr='lte')
    company_id = filters.CharFilter(field_name="equipment_id", lookup_expr="company_id")

    class Meta:
        model = EquipmentUpkeep
        fields = ["manager_name", "time_gt", "time_lt", "upkeep_man", "name", "company_id", "equipment_id"]


"""保养记录搜索查询"""
class EquipmentUpkeepViewSet(ModelViewSet):

    queryset = EquipmentUpkeep.objects.all()
    serializer_class = EquipmentUpkeepSerializer
    filterset_class = EquipmentupkeepFilter
    filter_backends = [OrderingFilter, DjangoFilterBackend]
    ordering_fields = ("time",)

    # def get_queryset(self):
    #
    #     query_dict = {}
    #     equipment = self.request.query_params.get("equipment", None)
    #     manager = self.request.query_params.get("manager", None)
    #     upkeep_man = self.request.query_params.get("upkeep_man", None)
    #     time = self.request.query_params.get("time", None)
    #     if equipment:
    #         if EquipmentInfo.objects.filter(name=equipment).count() == 0:
    #             return []
    #         query_dict["equipment_id"] = EquipmentInfo.objects.get(name=equipment).engineering_car_id
    #     if manager:
    #         if Staff.objects.filter(name=manager).count() == 0:
    #             return []
    #         query_dict["manager_id"] = Staff.objects.get(name=manager).staff_id
    #     if upkeep_man:
    #         if EquipmentUpkeep.objects.filter(upkeep_man=upkeep_man).count() == 0:
    #             return []
    #         query_dict["upkeep_man"] = upkeep_man
    #     if time:
    #         if EquipmentUpkeep.objects.filter(time=time).count() == 0:
    #             return []
    #         query_dict["time"] = time
    #
    #     queryset = EquipmentUpkeep.objects.filter(**query_dict)
    #
    #     return queryset