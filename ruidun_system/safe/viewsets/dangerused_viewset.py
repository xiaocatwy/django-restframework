import django_filters
from django_filters import rest_framework as filters
from rest_framework.decorators import action
from rest_framework.filters import OrderingFilter
from rest_framework.response import Response
from lib.model_viewset import ModelViewSet

from ..models import DangerUsed, Danger
from ..serializers.dangerused_serializer import DangerUsedSerializer
import numpy as np
import pandas as pd
import os


class DangerUsedFilter(django_filters.FilterSet):
    """危险品过滤器"""
    start_time = django_filters.DateFilter()
    start_time_gt = django_filters.DateFilter(field_name='start_time', lookup_expr='gt')
    start_time_lt = django_filters.DateFilter(field_name='start_time', lookup_expr='lte')
    end_time = django_filters.DateTimeFilter()
    end_time_gt = django_filters.DateTimeFilter(field_name='end_time', lookup_expr='gt')
    # danger = django_filters.CharFilter(field_name='danger_id', lookup_expr='name')
    # 物品分类
    category = django_filters.CharFilter(field_name='danger_id', lookup_expr='category_id')
    # 工区
    part_id = django_filters.CharFilter(field_name='danger_id', lookup_expr='part_id')
    manager = django_filters.CharFilter(field_name='manager_id', lookup_expr='name')
    user = django_filters.CharFilter(field_name='user_id', lookup_expr='name')

    class Meta:
        model = DangerUsed
        fields = ['start_time_gt', 'start_time_lt', 'end_time_gt', 'manager', 'user', 'danger', 'category', 'part_id']


class DangerUsedViewset(ModelViewSet):
    """危险物品管理"""

    # TODO 等待传入工区id
    queryset = DangerUsed.objects.all()
    serializer_class = DangerUsedSerializer
    filterset_class = DangerUsedFilter
    filter_backends = (OrderingFilter, filters.DjangoFilterBackend,)
    ordering_fields = ('id', 'start_time')

    # 导出
    @action(methods=["GET"], detail=False)
    def danger_used_out(self, request):
        id_str = request.query_params.get("list")
        if not id_str:
            return Response({"msg": "请勾选导出的内容"}, status=200)
        else:
            id_list = id_str.split(",")
            value = self.queryset.filter(id__in=id_list).values("danger_id__name", "manager_id__name", "user_id__name",
                                                                "count", "start_time", "end_time",
                                                                "danger__category__name")
            array = [list(array.values()) for array in value]
            for i in range(len(array)):
                array[i][4] = array[i][4].strftime("%Y-%m-%d %H:%M:%S")
                array[i][5] = array[i][5].strftime("%Y-%m-%d %H:%M:%S")
            excel = pd.DataFrame(np.array(array), columns=["物品名称", "负责人", "领用人", "领用数量", "领用日期", "归还日期", "物品分类"])
            filepath = "media/xlsx/danger_used.xlsx"
            if os.path.exists(filepath):
                os.remove(filepath)
            excel.to_excel(filepath)
            path = request.META.get('SERVER_PROTOCOL').split("/")[0].lower() + "://" + request.META.get(
                'HTTP_HOST') + "/" + filepath
            return Response({"path": path}, status=200)
