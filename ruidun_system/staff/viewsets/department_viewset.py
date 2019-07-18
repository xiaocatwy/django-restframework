# from lib.model_viewset import ModelViewSet
#
# from ..models import Department
# from ..serializers.department_serializer import DepartmentSerializer
#
#
# class DepartmentViewset(ModelViewSet):
#     """部门信息"""
#     queryset = Department.objects.filter(is_used=1).all()
#     serializer_class = DepartmentSerializer
from rest_framework.response import Response
from rest_framework import status

from lib.model_viewset import ModelViewSet
import django_filters as filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from ..models import Department
from ..serializers.department_serializer import DepartmentSerializer


class DepartmentFilter(filters.FilterSet):
    class Meta:
        model = Department
        fields = ["department", "part_id"]


class DepartmentViewset(ModelViewSet):
    """部门信息"""
    queryset = Department.objects.filter(is_used=1)
    serializer_class = DepartmentSerializer
    filterset_class = DepartmentFilter
    filter_backends = [OrderingFilter, DjangoFilterBackend]

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.is_used = 0
        instance.status = 2
        instance.save()
        return Response(status=status.HTTP_204_NO_CONTENT)
