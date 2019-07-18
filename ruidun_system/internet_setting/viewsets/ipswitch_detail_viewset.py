import django_filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from lib.model_viewset import ModelViewSet

from internet_setting.models import IPSwitchDetail
from internet_setting.serializers.ipswitch_detail_serializer import IPSwitchDetailSerializer


# class VoiceFilter(django_filters.FilterSet):
#     '''可以根据时间区间， 是否损坏， 厂家， 型号等来过滤'''
#
#     time__gt = django_filters.DateTimeFilter(field_name='time', lookup_expr='gt')
#     time__lt = django_filters.DateTimeFilter(field_name='time', lookup_expr='lt')
#
#     class Meta:
#         model = Voice
#         fields = ["time__gt", 'time__lt', 'status',  'factory', 'model']
#

class IPSwitchDetailViewSet(ModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    queryset = IPSwitchDetail.objects.all()
    serializer_class = IPSwitchDetailSerializer
    # permission_classes = [SelfPermission]
    # filterset_class = VoiceFilter
    # filter_backends = [OrderingFilter, DjangoFilterBackend]
    # ordering_fields = ('time', 'status', 'category_id')


