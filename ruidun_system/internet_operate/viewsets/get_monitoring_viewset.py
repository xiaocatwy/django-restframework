from rest_framework import viewsets


class GetMonitoringViewSet(viewsets.ReadOnlyModelViewSet):

    def retrieve(self, request, *args, **kwargs):
        # 获取视频内容，视频应该是实时传输的，这里应该怎么返回数据？
        pass
