from rest_framework import viewsets, status
from rest_framework.filters import OrderingFilter
from rest_framework.response import Response

from internet_setting.models import DeviceCategory
from internet_setting.serializers.device_category_serializer import DeviceCategorySerializer
from lib import model_viewset


class DeviceCategoryViewSet(model_viewset.ModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    queryset = DeviceCategory.objects.filter(is_used=1).all()
    serializer_class = DeviceCategorySerializer
    filter_backends = [OrderingFilter]
    ordering_fields = ('index',)

    # permission_classes = [SelfPermission]
    #
    # def destroy(self, request, *args, **kwargs):
    #     instance = self.get_object()
    #     instance.is_used = 0
    #     instance.save()
    #     return Response(status=status.HTTP_204_NO_CONTENT)

    # def destroy(self, request, *args, **kwargs):
    #     partial = kwargs.pop('partial', False)
    #     instance = self.get_object()
    #     serializer = self.get_serializer(instance, data=request.data, partial=partial)
    #     serializer.is_valid(raise_exception=True)
    #     instance.save()