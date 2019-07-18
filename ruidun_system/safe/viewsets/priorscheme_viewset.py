import os
import re
from time import time
import base64
import django_filters
from django_filters import rest_framework as filters
from rest_framework import status
from rest_framework.filters import OrderingFilter
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.parsers import MultiPartParser, FormParser,JSONParser
from rest_framework import permissions

from base_system import settings
from ..models import PriorScheme
from ..serializers.priorscheme_serializer import PriorSchemeSerializer
from lib.model_viewset import ModelViewSet


class PriorSchemeFilter(django_filters.FilterSet):
    """应急方案过滤器"""

    update_time = django_filters.DateTimeFilter()
    update_time_gt = django_filters.DateTimeFilter(field_name='update_time', lookup_expr='gt')
    update_time_lt = django_filters.DateTimeFilter(field_name='update_time', lookup_expr='lt')
    staff = django_filters.CharFilter(field_name='staff_id', lookup_expr='name')

    class Meta:
        model = PriorScheme
        fields = ['update_time_gt', 'update_time_lt', 'staff', 'name']


class PriorSchemeViewset(ModelViewSet):
    """应急方案管理"""

    queryset = PriorScheme.objects.filter(is_used=1)
    serializer_class = PriorSchemeSerializer

    filterset_class = PriorSchemeFilter
    filter_backends = (OrderingFilter, filters.DjangoFilterBackend)
    ordering_fields = ('update_time',)

    def update(self, request, *args, **kwargs):
        print(request.data)
        partial = kwargs.pop('partial', False)
        instance = self.get_object()

        data = dict(request.data)

        data = {key: value[0] for key, value in data.items()}
        # print(len(data.get("id_card_photo")))
        # path = data['path'].split('0/')[1]
        # base_path = settings.BASE_DIR + '/' + path
        #
        # if os.path.exists(base_path):
        #     del data["path"]
        del data["path"]
        serializer = self.get_serializer(instance, data=data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)

    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    # def create(self, request, *args, **kwargs):
    #
    #     # 获取上传文件
    #     texts = request.data.get('text')
    #
    #     if not texts:
    #         return Response({'error':'缺少上传文件'}, status=status.HTTP_400_BAD_REQUEST)
    #
    #     # 防止重名加入时间戳
    #     text_name = '%s_%s' % (time(), texts.name)
    #
    #     # 保存路径
    #     save_path = '%s/priorscheme/%s' % (settings.TEXT_ROOT, text_name)
    #
    #     with open(save_path, 'wb') as f:
    #
    #         # 防止上传文件过大
    #         for text in texts.chunks():
    #             f.write(text)
    #
    #     # 把路径加到request.data中
    #     r_dict = request.data
    #     r_dict['path'] = 'static/text/priorscheme/%s' % text_name
    #
    #     serializer = self.get_serializer(data=r_dict)
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save()
    #     headers = self.get_success_headers(serializer.data)
    #     return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
    #
    @action(methods=['get'], detail=True)
    def download(self, request, pk):
        """
        修改应急方案下载次数
        """

        # 获取文件下载路径，判断文件是否存在
        priorschem = self.get_object()
        path = priorschem.path
        base_path = settings.BASE_DIR + '/media' + '/' + str(path)

        if os.path.exists(base_path):

            priorschem = self.get_object()
            priorschem.download_times += 1
            priorschem.save()

            return Response({'download_times': priorschem.download_times}, status=status.HTTP_200_OK)

        else:
            return Response({'error': '下载文件不存在'}, status=status.HTTP_200_OK)
