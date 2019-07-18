from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
import django_filters as filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from ..models import Staff, UserWork
from ..serializers.usermouthwork_serializer import UserMouthWorkSerializer
import calendar
import datetime

class UserWorkWorkFilter(filters.FilterSet):
    """根据时间,姓名,部门查询出勤率"""
    department = filters.CharFilter(field_name="department_id", lookup_expr="name")
    class Meta:
        model = Staff
        fields = ["name", "department", "department_id", "part_id"]


class UserMouthWorkViewset(ModelViewSet):
    """月考勤信息时间排序在序列化器里面"""
    queryset = Staff.objects.all()
    serializer_class = UserMouthWorkSerializer
    filterset_class = UserWorkWorkFilter
    # filter_backends = [OrderingFilter, DjangoFilterBackend]
    # ordering_fields = ("staff_id__name", "time")
    # def get_queryset(self):
    # def list(self, request, *args, **kwargs):
    #     queryset = self.filter_queryset(self.get_queryset())
    #     print(request)
    #
    #     page = self.paginate_queryset(queryset)
    #     if page is not None:
    #         serializer = self.get_serializer(page, many=True, context={"time_limit": request.data.get("time_limit")})
    #         return self.get_paginated_response(serializer.data)
    #
    #     serializer = self.get_serializer(queryset, many=True, context={"time_limit": request.data.get("time_limit")})
    #     return Response(serializer.data)
