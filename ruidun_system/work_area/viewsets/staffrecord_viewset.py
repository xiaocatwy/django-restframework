import django_filters
from lib.model_viewset import ModelViewSet
from rest_framework.filters import OrderingFilter
from django_filters import rest_framework as filters

from ..models import StaffRecord
from staff.models import Staff
from ..serializers.staffrecord_serializer import StaffRecordSerializer
# 自定义
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
import numpy as np
import pandas as pd
import os


class StaffRecordFilter(django_filters.FilterSet):
    # 人员通行记录过滤器
    time = django_filters.DateTimeFilter()
    time_gt = django_filters.DateTimeFilter(field_name='time', lookup_expr='gt')
    time_lt = django_filters.DateTimeFilter(field_name='time', lookup_expr='lt')
    # staff = django_filters.CharFilter(field_name='staff_id', lookup_expr='name')

    class Meta:
        model = StaffRecord
        # fields = ['time_gt', 'time_lt', 'staff', 'staff_break']
        fields = ['time_gt', 'time_lt', 'device_name', 'names', 'part_id']


class StaffRecordViewset(ModelViewSet):
    """人员通行记录"""

    # TODO 等待传入工区id
    sysid = 'SYS0101'
    queryset = StaffRecord.objects.all().order_by('-time')
    serializer_class = StaffRecordSerializer
    filterset_class = StaffRecordFilter
    filter_backends = (OrderingFilter, filters.DjangoFilterBackend,)
    ordering_fields = ('time',)

    # 导出
    @action(methods=["GET"], detail=False)
    def staff_recode_out(self, request):
        id_str = request.query_params.get("list")
        if not id_str:
            return Response({"msg": "请勾选导出的内容"}, status=200)
        else:
            id_list = id_str.split(",")
            value = self.queryset.filter(id__in=id_list).values("card_number","names","device_name","inouts","time")
            array = [list(array.values()) for array in value]
            print(array)
            for i in range(len(array)):
                array[i][4] = array[i][4].strftime("%Y-%m-%d %H:%M:%S")
                if str(array[i][3]) == "in":
                    array[i][3] = "进入"
                else:
                    array[i][3] = "离开"
            excel = pd.DataFrame(np.array(array), columns=["人员通行证卡号", "姓名", "识别设备", "进出", "时间"])
            filepath = "media/xlsx/staff_recode.xlsx"
            if os.path.exists(filepath):
                os.remove(filepath)
            excel.to_excel(filepath)
            path = request.META.get('SERVER_PROTOCOL').split("/")[0].lower() + "://" + request.META.get(
                'HTTP_HOST') + "/" + filepath
            return Response({"path": path}, status=200)
