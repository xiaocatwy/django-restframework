import os
import re

from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.filters import OrderingFilter
from rest_framework.response import Response

from client.ipvoice import Client
from internet_setting.models import VoiceServer
from internet_setting.serializers.voice_server_serializer import VoiceServerSerializer
from lib import model_viewset


class VoiceServerViewSet(model_viewset.ModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    queryset = VoiceServer.objects.all()
    serializer_class = VoiceServerSerializer
    filter_backends = [OrderingFilter]
    # ordering_fields = ('index',)

    # @action(methods=['POST'], detail=True)
    # def voice(self, request, pk):
    #     "指定音响播放录音接口"
    #     obj = self.get_object()
    #     # print(obj.ip)
    #     # print(obj.port)
    #     voice_path = request.data.get('voice_path')
    #     snlist = request.data.get('snlist')  # 多个序列号之间用逗号隔开
    #     # print(voice_path, snlist)
    #     # 调用硬件接口：
    #     client = Client(ip=obj.ip, port=obj.port, voiceFilePath=voice_path, snlist=snlist)
    #     try:
    #         result = client.send()
    #         return Response(data=result, status=status.HTTP_200_OK)
    #     except Exception:
    #         return Response(data={"message": "硬件连接异常"}, status=status.HTTP_200_OK)

    @action(methods=['POST'], detail=True)
    def voice(self, request, pk):
        "指定音响播放录音接口"
        obj = self.get_object()
        # print(obj.ip)
        # print(obj.port)
        voice_path = request.data.get('voice_path')
        paths = re.search(r"m.*", voice_path).group()
        # voice_path = os.path.realpath(voice_path.split("8001/")[-1])
        voice_path = os.path.realpath(paths)
        snlist = request.data.get('snlist')  # 多个序列号之间用逗号隔开
        # print(voice_path, snlist)
        # 调用硬件接口：
        client = Client(ip=obj.ip, port=obj.port, voiceFilePath=voice_path, snlist=snlist)
        try:
            result = client.send()
            return Response(data=result, status=status.HTTP_200_OK)
        except Exception:
            return Response(data={"message": "音响设备连接异常"}, status=status.HTTP_200_OK)