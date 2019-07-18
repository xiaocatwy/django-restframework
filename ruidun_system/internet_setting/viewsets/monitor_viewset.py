import django_filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from lib.model_viewset import ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from internet_setting.models import LEDInfo, MonitorInfo
from internet_setting.serializers.led_serializer import LEDInfoSerializer
from internet_setting.serializers.monitor_serializer import MonitorInfoSerializer


class MonitorInfoFilter(django_filters.FilterSet):
    '''可以根据时间区间， 是否损坏， 厂家id， 型号， 分类等来过滤'''

    time__gt = django_filters.DateTimeFilter(field_name='time', lookup_expr='gt')
    time__lt = django_filters.DateTimeFilter(field_name='time', lookup_expr='lt')

    class Meta:
        model = MonitorInfo
        fields = ["time__gt", 'time__lt', 'status', 'factory', 'model']


class MonitorInfoViewSet(ModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    queryset = MonitorInfo.objects.all().order_by("number")
    serializer_class = MonitorInfoSerializer
    # permission_classes = [SelfPermission]
    filterset_class = MonitorInfoFilter
    filter_backends = [OrderingFilter, DjangoFilterBackend]
    ordering_fields = ('time', 'status')

    @action(methods=["GET"], detail=False)
    def monitor_order(self, request):
        id_list=[]
        monitor = MonitorInfo.objects.all().order_by("number")
        numbers = request.query_params.get("number_list")
        number_list = numbers.split(",")
        ids = monitor.values("id")
        for i in ids:
            id_list.append(i["id"])
        for i in range(len(number_list)):
            change = MonitorInfo.objects.get(id=id_list[i])
            change.number = number_list[i]
            change.save()
        return Response(data={"msg":"ok"}, status=200)



