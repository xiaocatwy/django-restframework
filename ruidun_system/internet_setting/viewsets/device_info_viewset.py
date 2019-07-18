import django_filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from lib.model_viewset import ModelViewSet

from internet_setting.models import DeviceInfo
from internet_setting.serializers.device_info_serializer import DeviceInfoSerializer


class DeviceInfoFilter(django_filters.FilterSet):
    '''可以根据时间区间， 是否损坏， 厂家id， 型号， 分类等来过滤'''

    time__gt = django_filters.DateTimeFilter(field_name='time', lookup_expr='gt')
    time__lt = django_filters.DateTimeFilter(field_name='time', lookup_expr='lt')

    class Meta:
        model = DeviceInfo
        fields = ["time__gt", 'time__lt', 'status', 'category_id', 'factory', 'model']


class DeviceInfoViewSet(ModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    queryset = DeviceInfo.objects.all()
    serializer_class = DeviceInfoSerializer
    # permission_classes = [SelfPermission]
    filterset_class = DeviceInfoFilter
    filter_backends = [OrderingFilter, DjangoFilterBackend]
    ordering_fields = ('time', 'status', 'category_id')



