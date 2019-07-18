import django_filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from rest_framework import viewsets

from internet_setting.models import BsTation
from internet_setting.serializers.bstation_serializer import BsTaionSerializer


class BsTaionViewSet(viewsets.ReadOnlyModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    queryset = BsTation.objects.all()
    serializer_class = BsTaionSerializer
    filter_fields = ("part_id",)