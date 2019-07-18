import django_filters
from django_filters import rest_framework as filters
from rest_framework.filters import OrderingFilter
from rest_framework.viewsets import ModelViewSet

from ..models import Danger
from ..serializers.dangername_serializer import DangerNameSerializer


class DangerFilter(django_filters.FilterSet):
    """危险品过滤器"""
    # start_time = django_filters.DateTimeFilter()
    # start_time_gt = django_filters.DateTimeFilter(field_name='start_time', lookup_expr='gt')
    # start_time_lt = django_filters.DateTimeFilter(field_name='start_time', lookup_expr='lte')
    # end_time = django_filters.DateTimeFilter()
    # end_time_gt = django_filters.DateTimeFilter(field_name='end_time', lookup_expr='gt')
    # # danger = django_filters.CharFilter(field_name='danger_id', lookup_expr='name')
    # # 物品分类
    # category = django_filters.CharFilter(field_name='danger_id', lookup_expr='category_id')
    # manager = django_filters.CharFilter(field_name='manager_id', lookup_expr='name')
    # user = django_filters.CharFilter(field_name='user_id', lookup_expr='name')

    class Meta:
        model = Danger
        fields = ['category_id', 'part_id']


class DangerNameViewset(ModelViewSet):
    """危险品名称（搜索）"""

    queryset = Danger.objects.filter(is_used=1)
    serializer_class = DangerNameSerializer
    filterset_class = DangerFilter
    filter_backends = (OrderingFilter, filters.DjangoFilterBackend,)
    ordering_fields = ('name',)
