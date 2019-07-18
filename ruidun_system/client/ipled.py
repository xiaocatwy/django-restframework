#coding=utf-8
from common.cfg import Config
from common.myfuncs import Funcs
from common.myproxy import Proxy

'''
ipled控制
'''
class Client:
    device='ipled' #设备类型
    token='...' #暂略

    # AddScreen
    nControlType = 340 #显示屏的控制器型号；详见宏定义“控制器型号定义”  Controller_BX_5E1 = 0x0154; 340
    nScreenNo = 1 #显示屏屏号；该参数与LedshowTW 2013软件中"设置屏参"模块的"屏号"参数一致。
    nSendMode = 2 #与显示屏的通讯模式； 2#网络模式
    nWidth = 96 #显示屏宽度 16的整数倍；最小64；BX-5E系列最小为80
    nHeight = 48 #显示屏高度 16的整数倍；最小16；

    nScreenType = 1 #显示屏类型；1：单基色；2：双基色；
    '''
              3：双基色；注意：该显示屏类型只有BX-4MC支持；同时该型号控制器不支持其它显示屏类型。
              4：全彩色；注意：该显示屏类型只有BX-5Q系列支持；同时该型号控制器不支持其它显示屏类型。
              5：双基色灰度；注意：该显示屏类型只有BX-5QS支持；同时该型号控制器不支持其它显示屏类型。
    '''
    nPixelMode = 1 #点阵类型；1：R+G；2：G+R；该参数只对双基色屏有效 ；默认为2；
    nDataDA = 0 #数据极性；，0x00：数据低有效，0x01：数据高有效；默认为0；
    nDataOE = 0 #OE极性；  0x00：OE 低有效；0x01：OE 高有效；默认为0；
    nRowOrder = 0 #行序模式；0：正常；1：加1行；2：减1行；默认为0；
    nDataFlow = 0 #扫描点频；0~6；默认为0；
    nFreqPar = 0 #扫描点频；0~6；默认为0；

    pCom = 'COM1' #串口名称；串口通讯模式时有效；例#COM1
    nBaud = 57600 #串口波特率：目前支持9600、57600；默认为57600；
    pSocketIP = '192.168.0.199' #控制卡IP地址，网络通讯模式时有效；例#192.168.0.199；
    nSocketPort = 5005 #控制卡网络端口；网络通讯模式时有效；例：5005
    nStaticIPMode = 0 #固定IP通讯模式  0：TCP模式  ；1：UDP模式
    nServerMode = 0 ##0#服务器模式未启动；1：服务器模式启动。
    pBarcode = '' #设备条形码

    pNetworkID = '' #服务器模式时的网络ID编号
    pServerIP = '112.65.245.174' #中转服务器IP地址
    nServerPort = 6055 #中转服务器网络端口
    pServerAccessUser = 'dyrbt' #中转服务器访问用户名
    pServerAccessPassword = '8336378' #中转服务器访问密码
    pWiFiIP = '192.168.100.1' #控制器WiFi模式的IP地址信息；WiFi通讯模式时有效；例#192.168.100.1

    nWiFiPort = 5005 #控制卡WiFi端口；WiFi通讯模式时有效；例：5005
    pGprsIP = '192.168.0.152' #GPRS服务器IP地址
    nGprsPort = 8120 #GPRS服务器端口
    pGprsID = 'BX-GP000001' #GPRS编号
    pScreenStatusFile = '' #用于保存查询到的显示屏状态参数保存的INI文件名；

    # AddScreenProgram
    # nScreenNo
    nProgramType = 0 #节目类型；0正常节目。
    nPlayLength = 0 #0#表示自动顺序播放；否则表示节目播放的长度；范围1~65535；单位秒

    nStartYear = 65535 #节目的生命周期；开始播放时间年份。如果为无限制播放的话该参数值为65535；如2010
    nStartMonth = 11 #节目的生命周期；开始播放时间月份。如11
    nStartDay = 26 #节目的生命周期；开始播放时间日期。如26
    nEndYear = 2099 #节目的生命周期；结束播放时间年份。如2099
    nEndMonth = 11 #节目的生命周期；结束播放时间月份。如11
    nEndDay = 26 #节目的生命周期；结束播放时间日期。如26

    nMonPlay = 1 #节目在生命周期内星期一是否播放;0：不播放;1：播放.
    nTuesPlay = 1 #节目在生命周期内星期二是否播放;0：不播放;1：播放.
    nWedPlay = 1 #节目在生命周期内星期二是否播放;0：不播放;1：播放.
    nThursPlay = 1 #节目在生命周期内星期二是否播放;0：不播放;1：播放.
    nFriPlay = 1 #节目在生命周期内星期二是否播放;0：不播放;1：播放.
    nSatPlay = 1 #节目在生命周期内星期二是否播放;0：不播放;1：播放.
    nSunPlay = 1 #节目在生命周期内星期二是否播放;0：不播放;1：播放.

    nStartHour = 0 #节目在当天开始播放时间小时。如8
    nStartMinute = 0 #节目在当天开始播放时间分钟。如0
    nEndHour = 23 #节目在当天结束播放时间小时。如18
    nEndMinute = 59 #节目在当天结束播放时间分钟。如0

    # AddScreenProgramBmpTextArea
    # nScreenNo
    nProgramOrd = 0 #节目序号；该序号按照节目添加顺序，从0顺序递增，如删除中间的节目，后面的节目序号自动填充。
    nX = 0 #区域的横坐标；显示屏的左上角的横坐标为0；最小值为0
    nY =  10 #区域的纵坐标；显示屏的左上角的纵坐标为0；最小值为0
    nAreaWidth = 96 #区域的宽度；最大值不大于显示屏宽度-nX
    nAreaHeight = 32 #区域的高度；最大值不大于显示屏高度-nY

    # AddScreenProgramAreaBmpTextText
    # nScreenNo
    # nProgramOrd
    nAreaOrd = 0 #区域序号；该序号按照区域添加顺序，从0顺序递增，如删除中间的区域，后面的区域序号自动填充。

    pText = 'Wellcome' #文本
    nShowSingle = 1 #单、多行显示；1：单行显示；0：多行显示；该参数只有在pFileName为txt类型文件时该参数才有效。
    nHorAlign = 1 #水平居中显示：0 居左 1居中 2 居右；
    nVerAlign = 0 #垂直居中显示：0 居中 1居上 2 居下；
    pFontName = '宋体' #字体名称；支持当前操作系统已经安装的矢量字库；该参数只有pFileName为txt类型文件时该参数才有效。
    nFontSize = 14 #字体字号；支持当前操作系统的字号；该参数只有pFileName为txt类型文件时该参数才有效。
    nBold = 1 #字体粗体；支持1：粗体；0：正常；该参数只有pFileName为txt类型文件时该参数才有效。
    nItalic =  0
    nUnderline = 0
    nFontColor = 255 #字体颜色；该参数只有pFileName为txt类型文件时该参数才有效。

    nStunt = 1 #显示特技。
    '''
              0x00#随机显示
              0x01#静态
              0x02#快速打出
              0x03#向左移动
              0x04#向左连移
              0x05#向上移动            3T类型控制卡无此特技
              0x06#向上连移            3T类型控制卡无此特技
              0x07#闪烁                3T类型控制卡无此特技
              0x08#飘雪
              0x09#冒泡
              0x0A#中间移出
              0x0B#左右移入
              0x0C#左右交叉移入
              0x0D#上下交叉移入
              0x0E#画卷闭合
              0x0F#画卷打开
              0x10#向左拉伸
              0x11#向右拉伸
              0x12#向上拉伸
              0x13#向下拉伸            3T类型控制卡无此特技
              0x14#向左镭射
              0x15#向右镭射
              0x16#向上镭射
              0x17#向下镭射
              0x18#左右交叉拉幕
              0x19#上下交叉拉幕
              0x1A#分散左拉
              0x1B#水平百页            3T、3A、4A、3A1、3A2、4A1、4A2、4A3、4AQ类型控制卡无此特技
              0x1C#垂直百页            3T、3A、4A、3A1、3A2、4A1、4A2、4A3、4AQ、3M、4M、4M1、4MC类型控制卡无此特技
              0x1D#向左拉幕            3T、3A、4A类型控制卡无此特技
              0x1E#向右拉幕            3T、3A、4A类型控制卡无此特技
              0x1F#向上拉幕            3T、3A、4A类型控制卡无此特技
              0x20#向下拉幕            3T、3A、4A类型控制卡无此特技
              0x21#左右闭合            3T类型控制卡无此特技
              0x22#左右对开            3T类型控制卡无此特技
              0x23#上下闭合            3T类型控制卡无此特技
              0x24#上下对开            3T类型控制卡无此特技
              0x25#向右连移
              0x26#向右连移
              0x27#向下移动            3T类型控制卡无此特技
              0x28#向下连移            3T类型控制卡无此特技
    '''
    nRunSpeed = 10 #运行速度；0~63；值越大运行速度越慢。
    nShowTime = 10 #停留时间；0~65525；单位0.5秒
    nStretch = 0 #拉伸，拉伸+，收缩-
    nShift = 0 #上下移，上移为-,下移为+

    # SendScreenInfo
    # nScreenNo
    nSendCmd = 41456 #通讯命令值
    '''
              SEND_CMD_PARAMETER =41471;  加载屏参数。
              SEND_CMD_SENDALLPROGRAM = 41456;  发送所有节目信息。
              SEND_CMD_POWERON =41727; 强制开机
              SEND_CMD_POWEROFF = 41726; 强制关机
              SEND_CMD_TIMERPOWERONOFF = 41725; 定时开关机
              SEND_CMD_CANCEL_TIMERPOWERONOFF = 41724; 取消定时开关机
              SEND_CMD_RESIVETIME = 41723; 校正时间。
              SEND_CMD_ADJUSTLIGHT = 41722; 亮度调整。
    '''
    nOtherParam1 = 0 #保留参数；0

    #定时关机
    nOnHour1 = 0 # 第一组定时开关的开机时间的小时
    nOnMinute1 = 0 # 第一组定时开关的开机时间的分钟
    nOffHour1 = 0  # 第一组定时开关的关机时间的小时
    nOffMinute1 = 0  # 第一组定时开关的关机时间的分钟
    nOnHour2 = 0  # 第二组定时开关的开机时间的小时
    nOnMinute2 = 0  # 第二组定时开关的开机时间的分钟
    nOffHour2 = 0 # 第二组定时开关的关机时间的小时
    nOffMinute2 = 0 # 第二组定时开关的关机时间的分钟
    nOnHour3 = 0 # 第三组定时开关的开机时间的小时
    nOnMinute3 = 0 # 第三组定时开关的开机时间的分钟
    nOffHour3 = 0 # 第三组定时开关的关机时间的小时
    nOffMinute3 = 0 # 第三组定时开关的关机时间的分钟

    #跳亮度
    nAdjustType = 0  # 亮度调整类型；0：手工调亮；1：定时调亮
    nHandleLight = 0  # 手工调亮的亮度值，只有nAdjustType=0时该参数有效。
    nHour1 = 0  # 第一组定时调亮时间的小时
    nMinute1 = 0  # 第一组定时调亮时间的分钟
    nLight1 = 0  # 第一组定时调亮的亮度值
    nHour2 = 0  # 第二组定时调亮时间的小时
    nMinute2 = 0  # 第二组定时调亮时间的分钟
    nLight2 = 0  # 第二组定时调亮的亮度值
    nHour3 = 0  # 第三组定时调亮时间的小时
    nMinute3 = 0  # 第三组定时调亮时间的分钟
    nLight3 = 0  # 第三组定时调亮的亮度值
    nHour4 = 0  # 第四组定时调亮时间的小时
    nMinute4 = 0  # 第四组定时调亮时间的分钟
    nLight4 = 0  # 第四组定时调亮的亮度值

    def __init__(self):
        self.device='ipled'
        self.cfg = Config()
        self.url = self.cfg.get('main', 'url') + "/device"
        pass

    def send(self):
        #参数示例
        data={}
        data["token"]=self.token
        data["device"]=self.device

        # AddScreen
        data['nControlType'] = self.nControlType
        data['nScreenNo'] = self.nScreenNo
        data['nSendMode'] = self.nSendMode
        data['nWidth'] = self.nWidth
        data['nHeight'] = self.nHeight

        data['nScreenType'] = self.nScreenType
        data['nPixelMode'] = self.nPixelMode
        data['nDataDA'] = self.nDataDA
        data['nDataOE'] = self.nDataOE
        data['nRowOrder'] = self.nRowOrder
        data['nDataFlow'] = self.nDataFlow
        data['nFreqPar'] = self.nFreqPar

        data['pCom'] = self.pCom
        data['nBaud'] = self.nBaud
        data['pSocketIP'] = self.pSocketIP
        data['nSocketPort'] = self.nSocketPort
        data['nStaticIPMode'] = self.nStaticIPMode
        data['nServerMode'] = self.nServerMode
        data['pBarcode'] = self.pBarcode

        data['pNetworkID'] = self.pNetworkID
        data['pServerIP'] = self.pServerIP
        data['nServerPort'] = self.nServerPort
        data['pServerAccessUser'] = self.pServerAccessUser
        data['pServerAccessPassword'] = self.pServerAccessPassword
        data['pWiFiIP'] = self.pWiFiIP

        data['nWiFiPort'] = self.nWiFiPort
        data['pGprsIP'] = self.pGprsIP
        data['nGprsPort'] = self.nGprsPort
        data['pGprsID'] = self.pGprsID
        data['pScreenStatusFile'] = self.pScreenStatusFile

        # AddScreenProgram
        # nScreenNo
        data['nProgramType'] = self.nProgramType
        data['nPlayLength'] = self.nPlayLength

        data['nStartYear'] = self.nStartYear
        data['nStartMonth'] = self.nStartMonth
        data['nStartDay'] = self.nStartDay
        data['nEndYear'] = self.nEndYear
        data['nEndMonth'] = self.nEndMonth
        data['nEndDay'] = self.nEndDay

        data['nMonPlay'] = self.nMonPlay
        data['nTuesPlay'] = self.nTuesPlay
        data['nWedPlay'] = self.nWedPlay
        data['nThursPlay'] = self.nThursPlay
        data['nFriPlay'] = self.nFriPlay
        data['nSatPlay'] = self.nSatPlay
        data['nSunPlay'] = self.nSunPlay

        data['nStartHour'] = self.nStartHour
        data['nStartMinute'] = self.nStartMinute
        data['nEndHour'] = self.nEndHour
        data['nEndMinute'] = self.nEndMinute

        # AddScreenProgramBmpTextArea
        # =self.nScreenNo
        data['nProgramOrd'] = self.nProgramOrd
        data['nX'] = self.nX
        data['nY'] = self.nY
        data['nAreaWidth'] = self.nAreaWidth
        data['nAreaHeight'] = self.nAreaHeight

        # AddScreenProgramAreaBmpTextText
        # nScreenNo
        # nProgramOrd
        data['nAreaOrd'] = self.nAreaOrd

        data['pText'] = self.pText
        data['nShowSingle'] = self.nShowSingle
        data['nHorAlign'] = self.nHorAlign
        data['nVerAlign'] = self.nVerAlign
        data['pFontName'] = self.pFontName
        data['nFontSize'] = self.nFontSize
        data['nBold'] = self.nBold
        data['nItalic'] = self.nItalic
        data['nUnderline'] = self.nUnderline
        data['nFontColor'] = self.nFontColor

        data['nStunt'] = self.nStunt
        data['nRunSpeed'] = self.nRunSpeed
        data['nShowTime'] = self.nShowTime
        data['nStretch'] = self.nStretch
        data['nShift'] = self.nShift

        # SendScreenInfo
        # nScreenNo
        data['nSendCmd'] = self.nSendCmd
        data['nOtherParam1'] = self.nOtherParam1

        #定时关机
        data['nOnHour1'] = self.nOnHour1
        data['nOnMinute1'] = self.nOnMinute1
        data['nOffHour1'] = self.nOffHour1
        data['nOffMinute1'] = self.nOffMinute1
        data['nOnHour2'] = self.nOnHour2
        data['nOnMinute2'] = self.nOnMinute2
        data['nOffHour2'] = self.nOffHour2
        data['nOffMinute2'] = self.nOffMinute2
        data['nOnHour3'] = self.nOnHour3
        data['nOnMinute3'] = self.nOnMinute3
        data['nOffHour3'] = self.nOffHour3
        data['nOffMinute3'] = self.nOffMinute3

        #调亮度
        data['nAdjustType'] = self.nAdjustType
        data['nHandleLight'] = self.nHandleLight
        data['nHour1'] = self.nHour1
        data['nMinute1'] = self.nMinute1
        data['nLight1'] = self.nLight1
        data['nHour2'] = self.nHour2
        data['nMinute2'] = self.nMinute2
        data['nLight2'] = self.nLight2
        data['nHour3'] = self.nHour3
        data['nMinute3'] = self.nMinute3
        data['nLight3'] = self.nLight3
        data['nHour4'] = self.nHour4
        data['nMinute4'] = self.nMinute4
        data['nLight4'] = self.nLight4

        result=Proxy.send(self.url,data)
        return result


if __name__ == '__main__':
    obj=Client()
    obj.nScreenNo=1
    obj.nProgramOrd=0
    obj.pText='阿斯顿或阿基的哈及'
    result=obj.send()
    print(result)
