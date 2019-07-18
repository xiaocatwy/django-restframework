#coding=utf-8
from common.cfg import Config
from common.myfuncs import Funcs
from common.myproxy import Proxy

'''
ipvoice语音客户端接口
'''
class Client:
    device='ipvoice' #设备类型
    token='...' #暂略

    ip="192.168.0.112"
    port=6002
    voiceFilePath="D:/tts2.mp3" #完整路径
    snlist="e9682bb1b27ba83368d3932d0d2bd241"  # 终端序列号列表，多个设备采用逗号分隔，如："e9682bb1b27ba83368d3932d0d2bd241,e9682bb1b27ba83368d3932d0d2bd241"

    def __init__(self,ip,port,voiceFilePath,snlist):
        self.cfg = Config()
        self.url = self.cfg.get('main', 'url') + "/device"

        self.ip=ip
        self.port=port
        self.voiceFilePath=voiceFilePath
        self.snlist=snlist

        pass

    def send(self):
        #参数示例
        data={}
        data["token"]=self.token
        data["device"]=self.device

        data["ip"]=self.ip
        data["port"]=Funcs.toInt(self.port)

        data["voiceFilePath"]=self.voiceFilePath
        data["snlist"]=self.snlist

        result=Proxy.send(self.url,data)
        return result #异常返回值为''，正确返回值为1

if __name__ == '__main__':
    obj=Client("192.168.0.112",6002,"D:/tts2.mp3","e9682bb1b27ba83368d3932d0d2bd241")
    result=obj.send()
    print(result)
