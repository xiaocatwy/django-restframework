import json
from queue import Queue
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from lib.model_viewset import ModelViewSet
from staff.viewsets import staff_viewset
from client.location import Client
from  staff.serializers import staff_serializer
# 获取指定卡号或所有卡号的实时定位信息
from internet_setting.models import LocationCard
from staff.models import Staff, Trades

class StaffLocationViewSet(ModelViewSet):

    @action(methods=['POST'], detail=False)
    def card_locations(self, request):
        """整型数字 卡号 id"""
        card_id = request.data.get('card_id')
        locationUrl = request.data.get('locationUrl')
        username = request.data.get('username')
        password = request.data.get('password')
        # 调用硬件接口：
        if not all([locationUrl, username, password]):
            return Response(data={'message': "参数不足"}, status=status.HTTP_400_BAD_REQUEST)
        else:
            client = Client(locationUrl, username, password)
            try:
                if not card_id:
                    result = client.getAllCardNowPos()
                    result = json.loads(result)
                    list = result["result"]

                    return Response(data=result, status=200)
                else:
                    result = client.getAllCardNowPos(card_id)
                    result = json.loads(result)
                    return Response(data=result, status=200)
            except Exception:
                return Response(data={"message": "定位设备连接异常"}, status=status.HTTP_200_OK)


# 查询指定区域中存在的卡号
    @action(methods=['POST'], detail=False)
    def area_cards(self, request):
        """区域 id"""
        area_ids = request.data.get('area_ids')
        locationUrl = request.data.get('locationUrl')
        username = request.data.get('username')
        password = request.data.get('password')
        if not all([area_ids, locationUrl, username, password]):
            return Response(data={'message': "参数不足"}, status=status.HTTP_400_BAD_REQUEST)
        # 调用硬件接口：
        client = Client(locationUrl, username, password)
        try:
            result = client.getCardByArea(area_ids)
            return Response(data=result, status=200)
        except Exception:
            return Response(data={"message": "定位设备连接异常"}, status=status.HTTP_200_OK)


# 查询当前区域所有卡的信息及所在区域
    @action(methods=['POST'], detail=False)
    def area_cards_info(self, request):
        """区域 id"""
        area_id = request.data.get('area_id')
        locationUrl = request.data.get('locationUrl')
        username = request.data.get('username')
        password = request.data.get('password')
        if not all([locationUrl, username, password]):
            return Response(data={'message': "参数不足"}, status=status.HTTP_400_BAD_REQUEST)
        # 调用硬件接口：
        client = Client(locationUrl, username, password)
        try:
            result = client.getNowInfo(area_id)
            result = json.loads(result)
            all_info = result["result"]["data"]
            staffs = Staff.objects.all()
            trades = Trades.objects.all()
            for card in all_info:
                name = staffs.filter(id=card.get("card_id"))
                card["name"] = name.values("name")[0]['name'] if name else '未命名'
                card["phone"] = name.values("phone")[0]["phone"] if name else "无"
                department = name.values("department__department")
                group = name.values("department__group_name")
                card["department"] = department[0]["department__department"]+"/"+group[0]["department__group_name"] if name else "无"
                color = name.values("trade_id")
                if color:
                    card["color"] = trades.filter(id=color[0]['trade_id']).values("colour")[0]["colour"]
                    card["trades_name"] = trades.filter(id=color[0]['trade_id']).values("trades_name")[0]["trades_name"]
                else:
                    card["color"] = "#575757"
                    card["trades_name"] = "无"
            return Response(data=result, status=200)
        except Exception:
            return Response(data={"message": "定位连接异常"}, status=status.HTTP_200_OK)


# 查询所有区域中卡的数量
    @action(methods=['GET'], detail=False)
    def area_card_nums(self, request):
        locationUrl = request.data.get('locationUrl')
        username = request.data.get('username')
        password = request.data.get('password')
        if not all([locationUrl, username, password]):
            return Response(data={'message': "参数不足"}, status=status.HTTP_400_BAD_REQUEST)
        # 调用硬件接口：
        client = Client(locationUrl, username, password)
        result = client.getAllAreaCardNum()
        return Response(data=result, status=200)

# 定卡号的历史记录
    @action(methods=['POST'], detail=False)
    def card_history(self, request):
        card_ids = request.data.get('card_ids')
        # 前段每次将时间戳+7200000(俩个小时)
        time = int(request.data.get('time'))
        time_end = int(request.data.get('time_end'))
        s = (time_end-time) // 600000
        locationUrl = request.data.get('locationUrl')
        username = request.data.get('username')
        password = request.data.get('password')
        if not all([locationUrl, username, password]):
            return Response(data={'message': "参数不足"}, status=status.HTTP_400_BAD_REQUEST)
        # 调用硬件接口：
        client = Client(locationUrl, username, password)
        list = []
        try:
            for i in range(s):
                end_time = int(time) + 600000
                result = client.getCardHistory(time=time, card_ids=card_ids, end_time=end_time)
                result = json.loads(result)
                all_data_list = result.get("result")
                if len(all_data_list) <= 100:
                    list += all_data_list
                else:
                    vaul_len = len(all_data_list) // 100
                    all_list = [all_data_list[i] for i in range(0, len(all_data_list), vaul_len)]
                    list += all_list
                time = time+600000
            return Response(data=list, status=200)
        except Exception:
            return Response(data={"message": "定位数据获取异常"}, status=status.HTTP_200_OK)




