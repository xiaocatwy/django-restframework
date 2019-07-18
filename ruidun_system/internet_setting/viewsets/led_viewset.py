import json

import django_filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.filters import OrderingFilter
from rest_framework.response import Response

from client.ipled import Client
from lib.model_viewset import ModelViewSet

from internet_setting.models import LEDInfo
from internet_setting.serializers.led_serializer import LEDInfoSerializer


class LEDInfoFilter(django_filters.FilterSet):
    '''可以根据时间区间， 是否损坏， 厂家id， 型号， 分类等来过滤'''

    time__gt = django_filters.DateTimeFilter(field_name='time', lookup_expr='gt')
    time__lt = django_filters.DateTimeFilter(field_name='time', lookup_expr='lt')

    class Meta:
        model = LEDInfo
        fields = ["time__gt", 'time__lt', 'status', 'factory', 'model']


class LEDInfoViewSet(ModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    queryset = LEDInfo.objects.all()
    serializer_class = LEDInfoSerializer
    # permission_classes = [SelfPermission]
    filterset_class = LEDInfoFilter
    filter_backends = [OrderingFilter, DjangoFilterBackend]
    ordering_fields = ('time', 'status')

    @action(methods=['POST'], detail=False)
    def control_led(self, request):
        client = Client()
        client.pText = request.data.get("pText", "")  # 控制显示文字
        client.nScreenNo = request.data.get("nScreenNo", "1")
        # client.nSendCmd = request.data.get("nSendCmd", "41456")
        client.nStunt = request.data.get("nStunt", "4")
        # print(client.pText)
        try:
            result = client.send()
            return Response(data=result, status=200)
        except Exception:
            return Response(data={"message": "LED屏幕连接异常"}, status=status.HTTP_200_OK)


