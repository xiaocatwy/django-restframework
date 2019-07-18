import django_filters as filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from lib import model_viewset
from ..models import Part
from ..serializers.part_serializer import PartSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
import numpy as np
import pandas as pd
import os


class PartFilter(filters.FilterSet):
    '''可以根据工区名称， 项目名称，公司名称等来过滤'''

    project_name = filters.CharFilter(field_name="project_id", lookup_expr="name")
    company_name = filters.CharFilter(field_name="project_id", lookup_expr="name")

    class Meta:
        model = Part
        fields = ["name", "project_name", "company_name"]


class PartViewset(model_viewset.ModelViewSet):
    """工区模型"""
    queryset = Part.objects.filter(is_used=1).all()
    serializer_class = PartSerializer
    filterset_class = PartFilter
    filter_backends = [OrderingFilter, DjangoFilterBackend]
    # ordering_fields = ()

    @action(methods=["GET"], detail=False)
    def part_out(self, request):
        id_str = request.query_params.get("list")
        if not id_str:
            return Response({"msg": "请勾选导出的内容"}, status=200)
        else:
            id_list = id_str.split(",")

            value = self.queryset.filter(id__in=id_list).values("name", "project_id__name",
                                                                "project_id__company_id__name", "manager",
                                                                "manager_phone")

            array = [list(array.values()) for array in value]

            excel = pd.DataFrame(np.array(array), columns=["工区信息", "所属项目", "所属公司", "负责人", "负责人电话"])

            filepath = "media/xlsx/part.xlsx"
            if os.path.exists(filepath):
                os.remove(filepath)
            excel.to_excel(filepath)
            path = request.META.get('SERVER_PROTOCOL').split("/")[0].lower() + "://" + request.META.get(
                'HTTP_HOST') + "/" + filepath
            return Response({"path": path}, status=200)
