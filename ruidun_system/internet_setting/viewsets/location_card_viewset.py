import django_filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from rest_framework import viewsets

from internet_setting.models import LocationCard
from internet_setting.serializers.location_card_serializer import LocationCardSerializer


class LocationCardFilter(django_filters.FilterSet):
    '''可以根据时间区间， 发放状态来过滤'''

    time__gt = django_filters.DateTimeFilter(field_name='time', lookup_expr='gt')
    time__lt = django_filters.DateTimeFilter(field_name='time', lookup_expr='lt')

    # 还会补充其他字段，暂保留

    class Meta:
        model = LocationCard
        fields = ["time__gt", 'time__lt', 'status']


class LocationCardViewSet(viewsets.ReadOnlyModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    queryset = LocationCard.objects.all()
    serializer_class = LocationCardSerializer
    # permission_classes = [SelfPermission]
    filterset_class = LocationCardFilter
    filter_backends = [OrderingFilter, DjangoFilterBackend]
    ordering_fields = ('time', 'status')
