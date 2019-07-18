import json

from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.filters import OrderingFilter
from rest_framework.request import Request
from rest_framework.response import Response

from client.ipswitch import Client
from internet_setting.models import VoiceServer, IPSwitch
from internet_setting.serializers.ipswitch_detail_serializer import IPSwitchDetailSerializer
from internet_setting.serializers.ipswitch_serializer import IPSwitchSerializer
from internet_setting.serializers.voice_server_serializer import VoiceServerSerializer
from lib import model_viewset


class IPSwitchViewSet(model_viewset.ModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    queryset = IPSwitch.objects.all()
    serializer_class = IPSwitchSerializer
    # filter_backends = [OrderingFilter]
    # ordering_fields = ('index',)
    # control = ["False", "False","False","False","False","False","False","False",]
    command = ["x", "x", "x", "x", "x", "x", "x", "x"]  # 初始命令

    @action(methods=["POST"], detail=True)
    def control_ipswitch(self, request, pk):
        """开关数据如何来保存，开关的ip和端口，每个开关控制的哪些东西"""
        # 一个表记录端口，ip，位置，等信息，另一个表分别记录开关8个路分别控制的什么，前端发送过来的数据包括id、确定对象，然后包含控制8路的列表
        # control:{"1":true, "3":false}
        obj = self.get_object()
        data = request.data.get("control", {})
        # self.control.clear()
        # self.control.extend(list(data))
        # data = eval(data)
        # print(type(data))
        # print(data)

        for ind, value in enumerate(data):
            self.command[ind] = "1" if value else "0"

        # for key, val in data.items():
        #     self.command[int(key)] = "1" if val else "0"  # 循环判断开和关，没有的端口不操作
        cmd = "setr=%s" % "".join(self.command)  # 拼接命令
        # print(cmd)
        client = Client(ip=obj.ip, port=obj.port, cmd=cmd)
        result = client.send()
        return Response(data={}, status=status.HTTP_200_OK)

    @action(methods=["GET"], detail=True)
    def get_status(self, request, pk):
        # 获取按开关状态
        # obj = self.get_object()
        # client = Client(ip=obj.ip, port=obj.port, cmd="state=?")
        # result = json.loads(client.send()).get("output")
        # status = {str(ind + 1): True if value == "1" else False for ind, value in enumerate(result)}
        # return Response(data=status, status=200)
        return Response(data={"1": "False", "2": "False", "3": "False", "4": "False", "5": "False", "6": False, "7": False, "8": False},status=200)
        # return Response(data={"1": self.control[0], "2": self.control[1], "3": self.control[2], "4": self.control[3],"5": self.control[4], "6": self.control[5], "7": False, "8": False}, status=200)
    # @action(methods=["GET"], detail=False)
    # def get_ipswitch(self, request):
    #     queryset = self.queryset
    #     serializer = self.get_serializer(queryset, many=True)
    #     data = serializer.data
    #     for s in self.queryset:
    #         # print(IPSwitchDetailSerializer(s.detail.all(), many=True).data)
    #         print(s.detail)
    #
    #     # data["detail"] = map(lambda s: IPSwitchDetailSerializer(s.detail.all(), many=True).data, self.queryset)
    #     return Response(data=data, status=status.HTTP_200_OK)

