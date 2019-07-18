from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from lib.model_viewset import ModelViewSet
import django_filters as filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter

# from lib.user_permission import SelfPermission
from ..models import EquipmentInfo
from ..serializers.equipmentinfo_serializer import EquipmentInfoSerializer, EquipmentinfosSerializer, EquipmentinfopSerializer

"""基础信息搜索查询"""
class EquipmentinfoFilter(filters.FilterSet):
    # company_name = filters.CharFilter(field_name="company_id", lookup_expr='name')
    class Meta:
        model = EquipmentInfo
        fields = ["factory", 'model', "company_id", "name", "part_id"]


class EquipmentInfoViewSet(ModelViewSet):

    queryset = EquipmentInfo.objects.filter().all()
    serializer_class = EquipmentInfoSerializer
    filterset_class = EquipmentinfoFilter
    filter_backends = [OrderingFilter, DjangoFilterBackend]
    ordering_fields = ("bought_time", "id")
    # permission_classes = [SelfPermission, IsAuthenticated]

    @action(methods=["GET"], detail=False)
    def get_names(self, request):
        query = self.queryset
        data = map(lambda obj: {"id": obj.id, "name": "%s" % obj.name}, query)
        return Response(data=data, status=200)


class EquipmentInfosViewSet(ModelViewSet):
    queryset = EquipmentInfo.objects.all()
    serializer_class = EquipmentinfosSerializer


class EquipmentInfopViewSet(ModelViewSet):
    queryset = EquipmentInfo.objects.all()
    serializer_class = EquipmentinfopSerializer