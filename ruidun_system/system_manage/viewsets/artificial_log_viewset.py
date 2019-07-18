import django_filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from rest_framework import viewsets
from django.db.models import Q

from lib.model_viewset import DestroyModelMixin
from system_manage.models import ArtificialLog
from system_manage.serializers.artificial_log_serializer import ArtificialLogSerializer


class ArtificialLogFilter(django_filters.FilterSet):
    '''可以根据作者名， 时间'''

    time_gt = django_filters.DateTimeFilter(field_name='time', lookup_expr='gt')
    time_lt = django_filters.DateTimeFilter(field_name='time', lookup_expr='lt')

    # name = django_filters.CharFilter(field_name='user_id', lookup_expr='username')

    class Meta:
        model = ArtificialLog
        fields = ["time_gt", 'time_lt', 'time', 'user']


class ArtificialLogViewSet(viewsets.ReadOnlyModelViewSet):
    """人工日志类视图"""

    queryset = ArtificialLog.objects.all().order_by('-time')
    serializer_class = ArtificialLogSerializer
    filterset_class = ArtificialLogFilter
    filter_backends = [OrderingFilter, DjangoFilterBackend]
    ordering_fields = ["time", "category_id"]

    # def get_queryset(self):
    #     query =  ArtificialLog.objects.filter(Q(level__lt=self.request.user.log_level) | Q(user=self.request.user))
    #     return query