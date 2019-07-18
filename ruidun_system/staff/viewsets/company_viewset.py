from lib import model_viewset
from rest_framework import permissions
import django_filters as filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter

from auth_system.models import Company
from lib.user_permission import SelfPermission

from staff.serializers import CompanySerializer
from rest_framework_tracking.mixins import LoggingMixin
from rest_framework.decorators import action
from rest_framework.response import Response
import numpy as np
import pandas as pd
import os


class CompanyFilter(filters.FilterSet):
    '''可以根据名称等来过滤'''

    class Meta:
        model = Company
        fields = ["name"]


class CompanyViewSet(model_viewset.ModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    queryset = Company.objects.filter(is_used=1).all()
    serializer_class = CompanySerializer
    filterset_class = CompanyFilter
    filter_backends = [OrderingFilter, DjangoFilterBackend]
    # permission_classes = [SelfPermission]
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    @action(methods=["GET"], detail=False)
    def company_out(self, request):
        id_str = request.query_params.get("list")
        if not id_str:
            return Response({"msg": "请勾选导出的内容"}, status=200)
        else:
            id_list = id_str.split(",")

            value = self.queryset.filter(id__in=id_list).values("name", "boss_name", "phone_num", "company_address")

            array = [list(array.values()) for array in value]

            excel = pd.DataFrame(np.array(array), columns=["公司名称", "联系人", "联系电话", "联系地址"])

            filepath = "media/xlsx/company.xlsx"
            if os.path.exists(filepath):
                os.remove(filepath)
            excel.to_excel(filepath)
            path = request.META.get('SERVER_PROTOCOL').split("/")[0].lower() + "://" + request.META.get(
                'HTTP_HOST') + "/" + filepath
            return Response({"path": path}, status=200)
