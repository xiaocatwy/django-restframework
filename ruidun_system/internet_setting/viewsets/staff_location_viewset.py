import django_filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.filters import OrderingFilter

from internet_setting.models import StaffLocation
from internet_setting.serializers.staff_location_serializer import StaffLocationSerializer


class StaffLocationFilter(django_filters.FilterSet):
    time_gt = django_filters.DateTimeFilter(field_name="time", lookup_expr='gte')
    time_lt = django_filters.DateTimeFilter(field_name="time", lookup_expr='lte')
    part_id = django_filters.CharFilter(field_name="location_card_id", lookup_expr='staff__part_id')
    location_card_id = django_filters.CharFilter()

    class Meta:
        model = StaffLocation
        fields = ["time_gt", "time_lt", 'part_id']


class StaffLocationViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = StaffLocation.objects.all()
    serializer_class = StaffLocationSerializer
    filterset_class = StaffLocationFilter
    filter_backends = [OrderingFilter, DjangoFilterBackend]
    ordering_fields = ("time",)
