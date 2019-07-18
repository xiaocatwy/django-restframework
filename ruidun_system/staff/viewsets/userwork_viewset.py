from lib.model_viewset import ModelViewSet
import django_filters as filters
from rest_framework.decorators import action
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from ..models import UserWork, Staff
from ..serializers.userwork_serializer import UserWorkSerializer
import numpy as np
import pandas as pd
import os


class UserWorkWorkFilter(filters.FilterSet):
    """根据时间,姓名,部门id查询出勤率"""
    # time_gt = filters.DateTimeFilter(field_name="staff", lookup_expr='time__gte')
    # time_lt = filters.DateTimeFilter(field_name="staff", lookup_expr='time__lte')
    # staff_name = filters.CharFilter(field_name="staff_id", lookup_expr="name")
    # department_id = filters.CharFilter(field_name="staff_id", lookup_expr="department__id")
    # class Meta:
    #     model = UserWork
    #     fields = ["time_gt", "time_lt", "staff_name", "department_id"]
    department = filters.CharFilter(field_name="department_id", lookup_expr="name")

    class Meta:
        model = Staff
        fields = ["name", "department", "department_id", "part_id"]


class UserWorkViewset(ModelViewSet):
    """岗位信息"""
    queryset = Staff.objects.all()
    serializer_class = UserWorkSerializer
    filterset_class = UserWorkWorkFilter

    @action(methods=["GET"], detail=False)
    def user_work_out(self, request):
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
                if id in id_list:
                    daywork = all_id.get("daywork")
                    for work in daywork:
                        list = [all_id["daytime"], all_id["department"], all_id["name"], work["work_time"],
                                str(work["enter_time"]) if work["enter_time"] else work["enter_time"], str(work["leave_time"]) if work["leave_time"] else work["leave_time"], work["detail"],]
                        array.append(list)
            excel = pd.DataFrame(np.array(array), columns=["日期", "部门", "姓名", "出勤状况", "进入时间", "离开时间", "备注"])
            filepath = "media/xlsx/user.xlsx"
            if os.path.exists(filepath):
                os.remove(filepath)
            excel.to_excel(filepath)
            path = request.META.get('SERVER_PROTOCOL').split("/")[0].lower() + "://" + request.META.get(
                'HTTP_HOST') + "/" + filepath
            return Response({"path": path}, status=200)

    @action(methods=["post"], detail=False)
    def work_detail(self, request):
        id = request.query_params.get("id")
        work_detail = request.query_params.get("detail")
        if not all([id,work_detail]):
            return Response({"msg":"请传入正确的参数"},status=200)
        else:
            userwork = UserWork.objects.all()
            detail = userwork.get(id=id)
            detail.detail = work_detail
            detail.save()
            return Response({"msg":"ok"},status=200)