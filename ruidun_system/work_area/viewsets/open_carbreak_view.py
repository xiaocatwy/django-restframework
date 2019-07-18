from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from work_area.models import CarBreak


class OpenCarbreak(APIView):
    """开启车辆道闸"""

    def get(self, request):

        id = request.query_params.get('id')
        action = request.query_params.get('action')

        # 校验参数是否有值
        if not all([id, action]):
            return Response({'error':'参数不足'}, status=status.HTTP_400_BAD_REQUEST)

        if action not in ("True", "False"):
            return Response({'error': '参数错误'}, status=status.HTTP_400_BAD_REQUEST)

        # 查看道闸是否存在
        carbreak = None
        try:
            carbreak = CarBreak.objects.get(id=id)
        except Exception as e:
            # 写入logger日志
            pass
        if not carbreak:
            return Response({'error':'车辆道闸不存在'}, status=status.HTTP_400_BAD_REQUEST)

        # 调用硬件接口
        state, message = 接口(id, action)  # TODO 改为车辆道闸接口

        data = {
            'state': state,
            'message': message
        }

        return Response(data, status=status.HTTP_200_OK)