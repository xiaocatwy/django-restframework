#coding=utf-8
import random

from common.cfg import Config
from common.myfuncs import Funcs
from common.myproxy import Proxy
import requests

'''
location定位客户端接口
'''
class Client:
    device='location' #设备类型
    token='...' #暂略

    apiver = "1.2.0"

    #认证参数
    username = "admin"
    passwordMD5 = "21232f297a57a5a743894a0e4a801fc3"
    loginPath="/position_sdk/ModularUser/User/login"
    locationUrl="http://192.168.0.158"

    def __init__(self,locationUrl,username,password):
        self.cfg = Config()
        self.url = self.cfg.get('main', 'url') + "/device"

        self.locationUrl=locationUrl
        self.username=username
        self.passwordMD5=Funcs.md5(password)

    '''
    def login(self,username,password):
        data = {}
        data["username"] = username
        data["password"] = Funcs.md5(password)
        data["http_api_version"] = self.apiver

        myProxy = Proxy(self.loginUrl)
        result = myProxy.postEx(data)
        print(result)
    '''

    def evacuateTmpArea(self,floor_id,area,z_start,z_end ): #5.9.1 撤离临时划定区域
        data={}
        data["token"]=self.token
        data["device"]=self.device

        data["loginUrl"]=self.locationUrl + self.loginPath
        data["username"]=self.username
        data["password"]=self.passwordMD5
        data["http_api_version"]=self.apiver

        data["cmd"]=self.locationUrl+"/position_sdk/ModularNowInfo/NowInfo/evacuateTmpArea"
        data["floor_id"]=floor_id #整型数字 	楼层 id 	必须
        data["area"]=area #数组 	划定的区域坐标信息 	是
        data["z_start"]=z_start #整型数字 	开始高度 	是
        data["z_end"]=z_end #整型数字 	结束高度 	是

        result=Proxy.send(self.url,data)
        return result #异常返回值为''，正确返回值为，如

    def evacuateArea(self,area_id_str): #5.9.2 撤离已有区域
        data={}
        data["token"]=self.token
        data["device"]=self.device

        data["loginUrl"]=self.locationUrl + self.loginPath
        data["username"]=self.username
        data["password"]=self.passwordMD5
        data["http_api_version"]=self.apiver

        data["cmd"]=self.locationUrl+"/position_sdk/ModularNowInfo/NowInfo/evacuateArea"
        data["area_id_str"]=area_id_str #数组  	区域 id 数组  	是

        result=Proxy.send(self.url,data)
        return result #异常返回值为''，正确返回值为，如{"type":1,"message":"Request success","result":[16479]}

    def callCardList(self,card_list): #5.9.3 呼叫卡号，card_list逗号分隔
        data={}
        data["token"]=self.token
        data["device"]=self.device

        data["loginUrl"]=self.locationUrl + self.loginPath
        data["username"]=self.username
        data["password"]=self.passwordMD5
        data["http_api_version"]=self.apiver

        data["cmd"]=self.locationUrl+"/position_sdk/ModularNowInfo/NowInfo/callCardList"
        data["card_list"]=card_list #数组  	卡号 id 数组 	是

        result=Proxy.send(self.url,data)
        return result #异常返回值为''，正确返回值为，如{"type":1,"message":"Request success","result":"18438,16479"}


    def getAllCardNowPos(self,card_id=None): #5.9.4 获取指定卡号或所有卡号的实时定位信息
        data={}
        data["token"]=self.token
        data["device"]=self.device

        data["loginUrl"]=self.locationUrl + self.loginPath
        data["username"]=self.username
        data["password"]=self.passwordMD5
        data["http_api_version"]=self.apiver

        data["cmd"]=self.locationUrl+"/position_sdk/ModularNowInfo/NowInfo/getAllCardNowPos"
        if card_id: data["card_id"]=card_id #整型数字 	卡号 id  	否

        result=Proxy.send(self.url,data)
        return result #异常返回值为''，正确返回值为，如{"type":1,"message":"Request success","result":{"18438":{"card_relative_z":1.5,"uuid":2,"utype":0,"floor_id":1,"card_id":18438,"static":true,"time":1553148514364,"y":1.2125836680006,"x":3.2918612590217,"z":1.5,"floor_name":"楼层1","building_id":"1","building_name":"建筑1","scene_id":"1","scene_name":"场景1"}}}


    def getAllAreaCardNum(self): #5.9.5查询所有区域中卡的数量
        data={}
        data["token"]=self.token
        data["device"]=self.device

        data["loginUrl"]=self.locationUrl + self.loginPath
        data["username"]=self.username
        data["password"]=self.passwordMD5
        data["http_api_version"]=self.apiver

        data["cmd"]=self.locationUrl+"/position_sdk/ModularNowInfo/NowInfo/getAllAreaCardNum"

        result=Proxy.send(self.url,data)
        return result #异常返回值为''，正确返回值为，如{"type":1,"message":"Request success","result":{"8":{"num":2,"name":"工作区"}}}


    def getAllAreaCardID(self): #5.9.6查询所有区域中卡号查询所有区域中卡号
        data={}
        data["token"]=self.token
        data["device"]=self.device

        data["loginUrl"]=self.locationUrl + self.loginPath
        data["username"]=self.username
        data["password"]=self.passwordMD5
        data["http_api_version"]=self.apiver

        data["cmd"]=self.locationUrl+"/position_sdk/ModularNowInfo/NowInfo/getAllAreaCardID"

        result=Proxy.send(self.url,data)
        return result #异常返回值为''，正确返回值为，如{"type":1,"message":"Request success","result":{"8":[18438,16479]}}

    def getNowInfo(self,area_id=None,blind=None,floor_id=None,page=None,limit=None): #5.9.7 查询当前所有卡的信息及所在区域
        data={}
        data["token"]=self.token
        data["device"]=self.device

        data["loginUrl"]=self.locationUrl + self.loginPath
        data["username"]=self.username
        data["password"]=self.passwordMD5
        data["http_api_version"]=self.apiver

        data["cmd"]=self.locationUrl+"/position_sdk/ModularNowInfo/NowInfo/getNowInfo"
        if area_id: data["area_id"]=area_id
        if blind: data["blind"]=blind
        if floor_id: data["floor_id"]=floor_id
        if page: data["page"]=page
        if limit: data["limit"]=limit

        result=Proxy.send(self.url,data)
        return result
    def getCardByArea(self, area_ids): #5.9.8 查询指定区域中存在的卡号
        data={}
        data["token"]=self.token
        data["device"]=self.device

        data["loginUrl"]=self.locationUrl + self.loginPath
        data["username"]=self.username
        data["password"]=self.passwordMD5
        data["http_api_version"]=self.apiver

        data["cmd"]=self.locationUrl+"/position_sdk/ModularNowInfo/NowInfo/getCardByArea"
        data["area_ids"]=area_ids

        result=Proxy.send(self.url,data)
        return result #异常返回值为''，正确返回值为，如{"type":1,"message":"Request success","result":{"8":[16479]}}

    def getAreaByCard(self,card_ids): #5.9.9 查询指定卡号所在的区域
        data={}
        data["token"]=self.token
        data["device"]=self.device

        data["loginUrl"]=self.locationUrl + self.loginPath
        data["username"]=self.username
        data["password"]=self.passwordMD5
        data["http_api_version"]=self.apiver

        data["cmd"]=self.locationUrl+"/position_sdk/ModularNowInfo/NowInfo/getAreaByCard"
        data["card_ids"]=card_ids

        result=Proxy.send(self.url,data)
        return result #异常返回值为''，正确返回值为，如{"type":1,"message":"Request success","result":{"1":[],"4":[],"9":[],"6":[],"7":[]}}


    '''查询历史数据
    '''

    #注：如果数据量太大，最多只会返回 5000 条数据，根据时间戳可以获取之后的数据。
    def getCardHistory(self,time,end_time=None ,data_flag=None,area_xy=None,card_ids=None ,area_ids=None ,building_id=None ,scene_id=None ,floor_id=None   ): #5.6.1 查询卡的历史信息
        data={}
        data["token"]=self.token
        data["device"]=self.device

        data["loginUrl"]=self.locationUrl + self.loginPath
        data["username"]=self.username
        data["password"]=self.passwordMD5
        data["http_api_version"]=self.apiver

        data["cmd"]=self.locationUrl+"/position_sdk/ModularHistory/History/getCardHistory"
        data["time"]=time #整型数字 	开始时间戳（毫秒） 是
        if end_time: data["end_time"]=end_time #整型数字 	结束时间戳（毫秒）
        if data_flag: data["data_flag"] = data_flag #整型数字 	是否平滑:0 不平滑 1 平滑
        if area_xy: data["area_xy"] = area_xy #数组 	区域坐标:[x 最小值，x 最大值，y 最小值， y 最大值]
        if card_ids: data["card_ids"] = card_ids #字符串 	卡号 id 多个卡号以逗号隔开
        if area_ids: data["area_ids"] = area_ids #字符串 	区域 id 多个区域以逗号隔开
        if building_id: data["building_id"] = building_id #整型数字 	建筑 id
        if scene_id: data["scene_id"] = scene_id  #整型数字 	场景 id
        if floor_id: data["floor_id"] = floor_id  #整型数字 	楼层 id

        result=Proxy.send(self.url,data)
        return result


    def getCardHistoryDataTime(self,start_time,end_time=None ,card_ids=None,building_id=None ,scene_id=None ,floor_id=None   ): #5.6.2 查询有历史消息的时间段
        data={}
        data["token"]=self.token
        data["device"]=self.device

        data["loginUrl"]=self.locationUrl + self.loginPath
        data["username"]=self.username
        data["password"]=self.passwordMD5
        data["http_api_version"]=self.apiver

        data["cmd"]=self.locationUrl+"/position_sdk/ModularHistory/History/getCardHistoryDataTime"
        data["start_time"]=start_time #整型数字 	开始时间戳（毫秒） 	是
        if end_time: data["end_time"]=end_time #整型数字 	结束时间戳（毫秒）
        if card_ids: data["card_ids"] = card_ids #数组 	卡号 id 数组
        if building_id: data["building_id"] = building_id #整型数字 	建筑 id
        if scene_id: data["scene_id"] = scene_id  #整型数字 	场景 id
        if floor_id: data["floor_id"] = floor_id  #整型数字 	楼层 id

        result=Proxy.send(self.url,data)
        return result

    def getAreaCardRecord(self,start_time=None ,end_time=None ,card_id=None,type=None ,area_id=None ,page=None  ,limit=None   ): #5.6.3 查询卡在区域中停留时长的历史信息
        data={}
        data["token"]=self.token
        data["device"]=self.device

        data["loginUrl"]=self.locationUrl + self.loginPath
        data["username"]=self.username
        data["password"]=self.passwordMD5
        data["http_api_version"]=self.apiver

        data["cmd"]=self.locationUrl+"/position_sdk/ModularHistory/History/getAreaCardRecord"
        if start_time: data["start_time"]=start_time #整型数字 	开始时间戳（毫秒） 	是
        if end_time: data["end_time"]=end_time #整型数字 	结束时间戳（毫秒）
        if card_id: data["card_id"] = card_id #整型数字 	卡号 id 数组
        if type: data["type"] = type #整型数字 	当前考勤状态 0 超时离开 1 正常离开
        if area_id: data["area_id"] = area_id  #整型数字 	区域 id
        if page: data["page"] = page  #整型数字 	页数
        if limit: data["limit"] = limit  #整型数字 	每页数据条数

        result=Proxy.send(self.url,data)
        return result

    def getCardFloorDataTime(self,card_id,start_time ,end_time=None ,   ): #5.6.4 指定卡号查询该卡号有数据的时间段和所在楼层
        data={}
        data["token"]=self.token
        data["device"]=self.device

        data["loginUrl"]=self.locationUrl + self.loginPath
        data["username"]=self.username
        data["password"]=self.passwordMD5
        data["http_api_version"]=self.apiver

        data["cmd"]=self.locationUrl+"/position_sdk/ModularHistory/History/getCardFloorDataTime"
        data["card_id"] = card_id #整型数字 	卡号 id 数组
        data["start_time"]=start_time #整型数字 	开始时间戳（毫秒） 	是
        if end_time: data["end_time"]=end_time #整型数字 	结束时间戳（毫秒）
        result=Proxy.send(self.url,data)
        return result


if __name__ == '__main__':
    obj=Client("http://192.168.0.158",'admin',"admin")

    result=obj.evacuateTmpArea(1,'1,1,100,100',0,3)
    print(result)
    result=obj.evacuateArea('8')
    print("evacuateArea('8')==》"+result)
    result=obj.callCardList('18438,16479')
    print("callCardList('18438,16479')==》"+result)
    result=obj.getAllCardNowPos('18438')
    print("getAllCardNowPos('18438')==》"+result)
    result=obj.getAllAreaCardNum()
    print("getAllAreaCardNum()==》"+result)
    result=obj.getAllAreaCardID()
    print("getAllAreaCardID()==》"+result)
    result=obj.getNowInfo()
    print("getNowInfo()==》"+result)
    result=obj.getCardByArea(8)
    print("getCardByArea(8)==》"+result)
    result=obj.getAreaByCard(16479)
    print("getAreaByCard(16479)==》"+result)


    result=obj.getCardHistory(1554105317393)
    print("getCardHistory(1554105317393)==》"+result)
    result=obj.getCardHistoryDataTime(1554105317393)
    print("getCardHistoryDataTime(1554105317393)==》"+result)


    result=obj.getAreaCardRecord()
    print("getAreaCardRecord()==》"+result)
    result=obj.getCardFloorDataTime(16479,1554105317393)
    print("getCardFloorDataTime(16479,1554105317393)==》"+result)