import django_filters as filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from lib import model_viewset
from auth_system.models import Project
from ..serializers.project_serializer import ProjectSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
import numpy as np
import pandas as pd
import os


class ProjectFilter(filters.FilterSet):
    '''可以根据项目名称，公司名称等来过滤'''

    company_name = filters.CharFilter(field_name="company_id", lookup_expr="name")

    class Meta:
        model = Project
        fields = ["name", "company_name"]


class ProjectViewset(model_viewset.ModelViewSet):
    """项目模型"""
    queryset = Project.objects.filter(is_used=1).all()
    serializer_class = ProjectSerializer
    filterset_class = ProjectFilter
    filter_backends = [OrderingFilter, DjangoFilterBackend]

    @action(methods=["GET"], detail=False)
    def project_out(self, request):
        id_str = request.query_params.get("list")
        if not id_str:
            return Response({"msg": "请勾选导出的内容"}, status=200)
        else:
            id_list = id_str.split(",")

            value = self.queryset.filter(id__in=id_list).values("name", "company_id__name", "manager", "manager_phone")

            array = [list(array.values()) for array in value]

            excel = pd.DataFrame(np.array(array), columns=["项目名称", "所属公司", "负责人", "负责人电话"])

            filepath = "media/xlsx/project.xlsx"
            if os.path.exists(filepath):
                os.remove(filepath)
            excel.to_excel(filepath)
            path = request.META.get('SERVER_PROTOCOL').split("/")[0].lower() + "://" + request.META.get(
                'HTTP_HOST') + "/" + filepath
            return Response({"path": path}, status=200)
