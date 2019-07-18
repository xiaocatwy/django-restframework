import django_filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from rest_framework import viewsets

from internet_setting.models import CautionRecord
from internet_setting.serializers.caution_record_serializer import CautionRecordSerializer


class CautionRecordFilter(django_filters.FilterSet):
    '''可以根据时间区间，报警设备分类id， 处置人姓名来过滤'''

    time__gt = django_filters.DateTimeFilter(field_name='time', lookup_expr='gt')
    time__lt = django_filters.DateTimeFilter(field_name='time', lookup_expr='lt')

    name = django_filters.CharFilter(field_name='disposer_id', lookup_expr='name')
    category_id = django_filters.CharFilter(field_name='device_id', lookup_expr='category_id')

    class Meta:
        model = CautionRecord
        fields = ["time__gt", 'time__lt', 'category_id', 'name', 'status']


class CautionRecordViewSet(viewsets.ReadOnlyModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    queryset = CautionRecord.objects.all()
    serializer_class = CautionRecordSerializer
    # permission_classes = [SelfPermission]
    filterset_class = CautionRecordFilter
    filter_backends = [OrderingFilter, DjangoFilterBackend]
    ordering_fields = ('id', 'time')