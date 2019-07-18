import os
from time import time

import django_filters
from django_filters import rest_framework as filters
from rest_framework.filters import OrderingFilter
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action

from safe.serializers.method_serializer import MethodSerializer
from ..models import SpecialScheme, Method
from ..serializers.specialscheme_serializer import SpecialSchemeSerializer
from base_system import settings
from lib.model_viewset import ModelViewSet


class MethodFilter(django_filters.FilterSet):
    """专项方案过滤器"""

    time_gt = django_filters.DateTimeFilter(field_name='time', lookup_expr='gt')
    time_lt = django_filters.DateTimeFilter(field_name='time', lookup_expr='lt')

    class Meta:
        model = Method
        fields = ['time_gt', 'time_lt', 'people']


class MethodViewset(ModelViewSet):
    """专项方案管理"""

    queryset = Method.objects.all()
    serializer_class = MethodSerializer
    filterset_class = MethodFilter
    filter_backends = (OrderingFilter, filters.DjangoFilterBackend,)
    ordering_fields = ('reate_time', 'update_time')

