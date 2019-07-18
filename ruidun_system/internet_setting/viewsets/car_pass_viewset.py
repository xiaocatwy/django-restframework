import django_filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from rest_framework import viewsets

from internet_setting.models import CarPass
from internet_setting.serializers.car_pass_serializer import CarPassSerializer
from work_area.models import CarInfo



class CarPassFilter(django_filters.FilterSet):
    '''可以根据时间区间，车主姓名， 车牌号来过滤'''

    # time__gt = django_filters.DateTimeFilter(field_name='time', lookup_expr='gt')
    # time__lt = django_filters.DateTimeFilter(field_name='time', lookup_expr='lt')
    #
    # name = django_filters.CharFilter(field_name='car_id', lookup_expr='car_owner')  # 车主姓名

    class Meta:
        # model = CarPass
        # fields = ["time__gt", 'time__lt', 'car_id', 'name']
        model = CarInfo
        fields = ['cphm', 'clxh']


class CarPassViewSet(viewsets.ReadOnlyModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    queryset = CarInfo.objects.all()
    serializer_class = CarPassSerializer
    # permission_classes = [SelfPermission]
    filterset_class = CarPassFilter
    filter_backends = [OrderingFilter, DjangoFilterBackend]
    ordering_fields = ('cphm',)