from lib.model_viewset import ModelViewSet
from rest_framework.filters import OrderingFilter
from django_filters import rest_framework as filters

from staff.models import Department
from work_area.serializers.department_serializer import DepartmentSerializer


class DepartmentViewset(ModelViewSet):
    """施工班组"""

    # TODO 等待传入当前工区id
    # part_id = 2
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer