import django_filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from lib.model_viewset import ModelViewSet

from internet_setting.models import DeviceUpkeep
from internet_setting.serializers.device_upkeep_serializer import DeviceUpkeepSerializer


class DeviceUpkeepFilter(django_filters.FilterSet):
    '''可以根据时间区间，负责人， 维护人来过滤'''

    time__gt = django_filters.DateTimeFilter(field_name='time', lookup_expr='gt')
    time__lt = django_filters.DateTimeFilter(field_name='time', lookup_expr='lt')

    manager = django_filters.CharFilter(field_name='manager_id', lookup_expr='name')  # 负责人

    class Meta:
        model = DeviceUpkeep
        fields = ["time__gt", 'time__lt', 'manager', 'upkeep_man']


class DeviceUpkeepViewSet(ModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    queryset = DeviceUpkeep.objects.all()
    serializer_class = DeviceUpkeepSerializer
    # permission_classes = [SelfPermission]
    filterset_class = DeviceUpkeepFilter
    filter_backends = [OrderingFilter, DjangoFilterBackend]
    ordering_fields = ('time',)