from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from internet_setting.models import DeviceInfo


class LedViewSet(ViewSet):
    "音箱相关接口"

    @action(methods=['post'], detail=False)
    def control(self, request):
        "控制led开关的接口"
        part_id = request.data.get('part_id')
        ids = request.data.get('ids', [])
        act = request.data.get('action')
        if not all([part_id, ids, act]):
            return Response(data={'message': "参数不足"}, status=status.HTTP_400_BAD_REQUEST)
        # 校验操作方式和操作ids是否符合规则
        if act not in ["open", "down"]:
            return Response(data={'message': "操作方式错误"}, status=status.HTTP_400_BAD_REQUEST)
        if DeviceInfo.objects.filter(id__in=ids).count() != len(ids):
            return Response(data={'message': "操作LED id错误，部分id不存在"}, status=status.HTTP_400_BAD_REQUEST)

        # 调用硬件接口：
        result, message = 开启led接口(part_id = part_id, ids=ids, act=act)
        return Response(data={"reslut": result, "message":message}, status=status.HTTP_200_OK)

    @action(methods=['post'], detail=False)
    def voice(self, request):
        "控制音箱播放的接口"
        part_id = request.data.get('part_id')
        ids = request.data.get('ids', [])
        content = request.data.get('content')
        font = request.data.get('font')
        size = request.data.get('size')
        if not all([ids, content, font, size, part_id]):
            return Response(data={'message': "参数不足"}, status=status.HTTP_400_BAD_REQUEST)
        # 校验操作方式和操作ids是否符合规则
        if DeviceInfo.objects.filter(id__in=ids).count() != len(ids):
            return Response(data={'message': "操作音箱id错误，部分id不存在"}, status=status.HTTP_400_BAD_REQUEST)

        # 调用硬件接口：
        result, message = 控制led显示接口(part_id=part_id, ids=ids, content=content, font=font, size=size)
        return Response(data={"reslut": result, "message": message}, status=status.HTTP_200_OK)