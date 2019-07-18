import django_filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from rest_framework import viewsets

from auth_system.models import Company
from internet_setting.models import StaffPass
from internet_setting.serializers.staff_pass_serializer import StaffPassSerializer

class StaffPassFilter(django_filters.FilterSet):
    # time = django_filters.DateTimeFilter()
    time__gt = django_filters.DateTimeFilter(field_name='time', lookup_expr='gt')
    time__lt = django_filters.DateTimeFilter(field_name='time', lookup_expr='lt')
    # company = django_filters.ModelChoiceFilter(to_field_name="name", queryset=Company.objects.all())
    staff = django_filters.CharFilter(field_name='staff_id', lookup_expr='name')
    class Meta:
        model = StaffPass
        fields = ["time__gt", 'time__lt', 'status', 'staff']


class StaffPassViewSet(viewsets.ReadOnlyModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    queryset = StaffPass.objects.all()
    serializer_class = StaffPassSerializer
    # filter_fields = {
    #     'time': ['gt', 'lt']
    # }
    filterset_class = StaffPassFilter
    # filter_fields = ('status', 'staff_id')
    filter_backends = [OrderingFilter, DjangoFilterBackend]  # 为了兼容排序和过滤能同时有效
    ordering_fields = ('status', 'time')


    # permission_classes = [SelfPermission]

    # def get_queryset(self):
    #     company_id = self.request.query_params.get("company_id", None)
    #     staff = self.request.query_params.get("staff", None)
    #     status = self.request.query_params.get("status", None)
    #     start_time = self.request.query_params.get('start_time', None)
    #     end_time = self.request.query_params.get('end_time', None)
    #     conditions = {}  # 查询的条件
    #
    #     if staff:
    #         conditions["staff"] = staff
    #     if status:
    #         conditions["status"] = status
    #     if start_time:
    #         conditions['time__gt'] = start_time
    #     if end_time:
    #         conditions['time__lt'] = end_time
    #
    #
    #     queryset = StaffPass.objects.filter(**conditions).all()
    #     return queryset