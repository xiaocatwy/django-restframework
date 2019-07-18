from lib.model_viewset import ModelViewSet
import django_filters as filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from rest_framework.decorators import action
from rest_framework.response import Response
from staff.models import Department
from ..serializers.departmentwork_serializer import DepartmentworkSerializer
import numpy as np
import pandas as pd
import os

class DepartmentWorkFilter(filters.FilterSet):
    '''根据时间和部门查询出勤率'''
    # TODO 增加part_id
    class Meta:
        model = Department
        fields = ["department", "id", "part_id"]



class DepartmentworkViewset(ModelViewSet):
    """部门考勤信息"""
    queryset = Department.objects.all()
    serializer_class = DepartmentworkSerializer
    filterset_class = DepartmentWorkFilter
    # filter_backends = [OrderingFilter, DjangoFilterBackend]


    @action(methods=["GET"], detail=False)
    def department_work_out(self, request):
        id_str = request.query_params.get("list")
        if not id_str:
            return Response({"msg": "请勾选导出的内容"}, status=200)
        else:
            id_list = id_str.split(",")
            queryset = self.filter_queryset(self.get_queryset())
            serializer = self.get_serializer(queryset, many=True)
            array = []
            for all_id in serializer.data:
                id = all_id.get("id")
                if str(id) in id_list:
                    list = [all_id["time"], all_id["department"], all_id["fact"], all_id["real"], all_id["rate"]]
                    array.append(list)
            excel = pd.DataFrame(np.array(array), columns=["日期", "部门", "应到人数", "实到人数", "出勤率"])
            filepath = "media/xlsx/department.xlsx"
            if os.path.exists(filepath):
                os.remove(filepath)
            excel.to_excel(filepath)
            path = request.META.get('SERVER_PROTOCOL').split("/")[0].lower() + "://" + request.META.get(
                'HTTP_HOST') + "/" + filepath
            return Response({"path": path}, status=200)
