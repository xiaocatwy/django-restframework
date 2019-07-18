import django_filters
from django.conf import settings
from rest_framework.filters import OrderingFilter
from lib.model_viewset import ModelViewSet
from django_filters import rest_framework as filters

from ..models import CarRecord, CarInfo, CarBreak
from ..serializers.carrecord_serializer import CarRecordSerializer
# 自定义
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
import numpy as np
import pandas as pd
import os


class CarRecordFilter(django_filters.FilterSet):
    # 车辆通行记录过滤器
    time = django_filters.DateTimeFilter()
    time_gt = django_filters.DateTimeFilter(field_name='intime', lookup_expr='gt')
    time_lt = django_filters.DateTimeFilter(field_name='intime', lookup_expr='lt')
    # # 车牌号
    # car_number = django_filters.CharFilter(field_name='car_id', lookup_expr='id')
    # # 车主
    # car_owner = django_filters.CharFilter(field_name='car_id', lookup_expr='car_owner')

    class Meta:
        model = CarRecord
        # fields = ['time_gt', 'time_lt', 'car_number', 'car_owner', 'car_break']
        fields = ['time_gt', 'time_lt', 'cardnumber', 'inplace', 'outplace', 'part_id']


class CarRecordViewset(ModelViewSet):
    """车辆通行记录"""

    # sysid = 'SYS0101'
    queryset = CarRecord.objects.all().order_by('-intime')
    serializer_class = CarRecordSerializer
    filterset_class = CarRecordFilter
    filter_backends = (OrderingFilter, filters.DjangoFilterBackend,)
    ordering_fields = ('intime',)

    # 导出
    @action(methods=["GET"], detail=False)
    def car_recode_out(self, request):
        id_str = request.query_params.get("list")
        if not id_str:
            return Response({"msg": "请勾选导出的内容"}, status=200)
        else:
            id_list = id_str.split(",")
            value = self.queryset.filter(id__in=id_list).values("cardnumber", "inplace", "intime", "outplace", "outtime")
            array = [list(array.values()) for array in value]
            for i in range(len(array)):
                array[i][2] = array[i][2].strftime("%Y-%m-%d %H:%M:%S")
                array[i][4] = array[i][4].strftime("%Y-%m-%d %H:%M:%S")
            excel = pd.DataFrame(np.array(array), columns=["车牌号",  "进入闸道", "进入时间" ,"离开道闸", "离开时间"])
            filepath = "media/xlsx/car_recode.xlsx"
            if os.path.exists(filepath):
                os.remove(filepath)
            excel.to_excel(filepath)
            path = request.META.get('SERVER_PROTOCOL').split("/")[0].lower() + "://" + request.META.get('HTTP_HOST') + "/" + filepath
            return Response({"path": path}, status=200)
