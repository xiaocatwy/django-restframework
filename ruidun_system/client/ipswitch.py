#coding=utf-8
from common.cfg import Config
from common.myfuncs import Funcs
from common.myproxy import Proxy

'''
ipswitch开关客户端接口
'''
class Client:
    device='ipswitch' #设备类型
    token='...' #暂略

    ip="192.168.1.166"
    port=1234
    cmd = "device=?"

    '''
    #命令示例
    cmd = "device=?"  #查看设备信息，返回值：{"sn":"0369127442293896","devicename":"0369127442293896","hver":"ZMRN0808-V6M","mqtt_user":"","mqtt_psw":"","ip":"192.168.1.166","tcport":1234,"cmd":"device"}
    cmd = "restart=?" #重启设备，返回值：{"sn":"0369127442293896","cmd":"restart"}
    cmd = "state=?" #查询设备状态，返回值：{"cmd":"state","output":"10000000","input":"00000000","sn":"0369127442293896"}
    cmd = "setr=1x0xxxxx" #输出控制,setr=输出值，返回值{"cmd":"setr","output":"10000000","input":"00000000","sn":"0369127442293896"}
    '''

    '''
    发送:setr=输出值
    8 通道输出值为 8 字节，
    ’0’表示关，’1’表示 开，’2’表示点触，’3’表示翻转，’4’表示互锁，’x’表示不动作。 
    ‘2’:表示点动输出，实现打开，然后延时，然后自动关闭。 
    ‘3’：表示翻转，以前开，翻转后为关；以前是关，翻转后是开。
    ’4’:表示相邻 2 个互锁；互锁为 1-2，3-4，5-6 这样成对出现。 如果成对的控制中，不能出现 14 或 24 命令。 
    例如控制继电器 1 打开，则发送字符串 setr=1xxxxxxx 控制继电器 2 关闭，则发送字符串 setr=x0xxxxxx 

    output 表示输出状态，1 表示有输出，0 表示无输出 
    input 表示输入状态，1 表示有输入，0 表示无输入 

    '''

    def __init__(self,ip,port,cmd):
        self.cfg = Config()
        self.url = self.cfg.get('main', 'url') + "/device"

        self.ip=ip
        self.port=port
        self.cmd=cmd

        pass

    def send(self):
        #参数示例
        data={}
        data["token"]=self.token
        data["device"]=self.device

        data["ip"]=self.ip
        data["port"]=Funcs.toInt(self.port)

        data["cmd"]=self.cmd

        result=Proxy.send(self.url,data)
        return result

if __name__ == '__main__':
    obj=Client("192.168.1.166",1234,"setr=1x1xxxxx")
    result=obj.send()
    print(result)
