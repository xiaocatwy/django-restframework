import django_filters
from rest_framework.response import Response

from internet_setting.models import DeviceInfo
from internet_setting.serializers.device_info_serializer import DeviceInfoSerializer
from lib.model_viewset import ModelViewSet


class DeviceInfoFilter(django_filters.FilterSet):
    # 工区设备信息过滤器
    staff = django_filters.CharFilter(field_name='staff_id', lookup_expr='name')
    company = django_filters.CharFilter(field_name='part_id', lookup_expr='company_id__name')


    class Meta:
        model = DeviceInfo
        fields = ['category', 'name', 'factory', 'model', 'staff']


class DeviceInfoViewset(ModelViewSet):
    """工区设备信息"""

    queryset = DeviceInfo.objects.all()
    serializer_class = DeviceInfoSerializer
    filterset_class = DeviceInfoFilter

    # def list(self, request, *args, **kwargs):
    #
    #     # 获取到分类id
    #     device_category_id = request.query_params.get('id')
    #
    #     # 过滤
    #     queryset = self.filter_queryset(self.get_queryset())
    #     # 分页
    #     page = self.paginate_queryset(queryset)
    #     if page is not None:
    #         serializer = DeviceInfoSerializer(queryset, many=True)
    #         return self.get_paginated_response(serializer.data)
    #     # 序列化
    #     serializer = DeviceInfoSerializer(queryset, many=True)
    #     data = serializer.data
    #     return Response(serializer.data)