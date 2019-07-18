#coding=utf-8
import sys
import socket
import random
import time
import io
import threading
import logging

from common.myfuncs import Funcs

#
#高铭 20190206
#
class Task:
    #参数
    cmd=""

    result=""

    ledServerIP = "192.168.0.199"
    ledServerPort = 5005

    # AddScreen
    nControlType = '0'
    nScreenNo = '0'
    nSendMode = '0'
    nWidth = '0'
    nHeight = '0'

    nScreenType = '0'
    nPixelMode = '0'
    nDataDA = '0'
    nDataOE = '0'
    nRowOrder = '0'
    nDataFlow = '0'
    nFreqPar = '0'

    pCom = ''
    nBaud = '0'
    pSocketIP = ''
    nSocketPort = '0'
    nStaticIPMode = '0'
    nServerMode = '0'
    pBarcode = ''

    pNetworkID = ''
    pServerIP = ''
    nServerPort = ''
    pServerAccessUser = ''
    pServerAccessPassword = ''
    pWiFiIP = ''

    nWiFiPort = ''
    pGprsIP = ''
    nGprsPort = ''
    pGprsID = ''
    pScreenStatusFile = ''

    # AddScreenProgram
    # nScreenNo
    nProgramType = ''
    nPlayLength = ''

    nStartYear = ''
    nStartMonth = ''
    nStartDay = ''
    nEndYear = ''
    nEndMonth = ''
    nEndDay = ''

    nMonPlay = ''
    nTuesPlay = ''
    nWedPlay = ''
    nThursPlay = ''
    nFriPlay = ''
    nSatPlay = ''
    nSunPlay = ''

    nStartHour = ''
    nStartMinute = ''
    nEndHour = ''
    nEndMinute = ''

    # AddScreenProgramBmpTextArea
    # nScreenNo
    nProgramOrd = ''
    nX = ''
    nY = ''
    nAreaWidth = ''
    nAreaHeight = ''

    # AddScreenProgramAreaBmpTextText
    # nScreenNo
    # nProgramOrd
    nAreaOrd = ''

    pText = ''
    nShowSingle = ''
    nHorAlign = ''
    nVerAlign = ''
    pFontName = ''
    nFontSize = ''
    nBold = ''
    nItalic = ''
    nUnderline = ''
    nFontColor = 0

    nStunt = 0
    nRunSpeed = 0
    nShowTime = 0
    nStretch = 0
    nShift = 0

    # SendScreenInfo
    # nScreenNo
    nSendCmd = 0
    nOtherParam1 = 0

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

    def __init__(self,ledServerIP,ledServerPort):
        self.ledServerIP=ledServerIP
        self.ledServerPort=ledServerPort

        #threading.Thread.__init__(self)
        self.working=False
        self.result=""
        return

    def base64(self,s):
        return Funcs.base64encode(s)

    def toStr(self):
        msg=""

        # AddScreen
        msg = str(self.nControlType)
        msg = msg +'|'+ str(self.nScreenNo)
        msg = msg +'|'+ str(self.nSendMode)
        msg = msg +'|'+ str(self.nWidth)
        msg = msg +'|'+ str(self.nHeight)

        msg = msg +'|'+ str(self.nScreenType)
        msg = msg +'|'+ str(self.nPixelMode)
        msg = msg +'|'+ str(self.nDataDA)
        msg = msg +'|'+ str(self.nDataOE)
        msg = msg +'|'+ str(self.nRowOrder)
        msg = msg +'|'+ str(self.nDataFlow)
        msg = msg +'|'+ str(self.nFreqPar)

        msg = msg +'|'+ self.base64(self.pCom)
        msg = msg +'|'+ str(self.nBaud)
        msg = msg +'|'+ self.base64(self.pSocketIP)
        msg = msg +'|'+ str(self.nSocketPort)
        msg = msg +'|'+ str(self.nStaticIPMode)
        msg = msg +'|'+ str(self.nServerMode)
        msg = msg +'|'+ self.base64(self.pBarcode)

        msg = msg +'|'+ self.base64(self.pNetworkID)
        msg = msg +'|'+ self.base64(self.pServerIP)
        msg = msg +'|'+ str(self.nServerPort)
        msg = msg +'|'+ self.base64(self.pServerAccessUser)
        msg = msg +'|'+ self.base64(self.pServerAccessPassword)
        msg = msg +'|'+ self.base64(self.pWiFiIP)

        msg = msg +'|'+ str(self.nWiFiPort)
        msg = msg +'|'+ self.base64(self.pGprsIP)
        msg = msg +'|'+ str(self.nGprsPort)
        msg = msg +'|'+ self.base64(self.pGprsID)
        msg = msg +'|'+ self.base64(self.pScreenStatusFile)

        # AddScreenProgram
        # nScreenNo
        msg = msg +'|'+ str(self.nProgramType)
        msg = msg +'|'+ str(self.nPlayLength)

        msg = msg +'|'+ str(self.nStartYear)
        msg = msg +'|'+ str(self.nStartMonth)
        msg = msg +'|'+ str(self.nStartDay)
        msg = msg +'|'+ str(self.nEndYear)
        msg = msg +'|'+ str(self.nEndMonth)
        msg = msg +'|'+ str(self.nEndDay)

        msg = msg +'|'+ str(self.nMonPlay)
        msg = msg +'|'+ str(self.nTuesPlay)
        msg = msg +'|'+ str(self.nWedPlay)
        msg = msg +'|'+ str(self.nThursPlay)
        msg = msg +'|'+ str(self.nFriPlay)
        msg = msg +'|'+ str(self.nSatPlay)
        msg = msg +'|'+ str(self.nSunPlay)

        msg = msg +'|'+ str(self.nStartHour)
        msg = msg +'|'+ str(self.nStartMinute)
        msg = msg +'|'+ str(self.nEndHour)
        msg = msg +'|'+ str(self.nEndMinute)

        # AddScreenProgramBmpTextArea
        # nScreenNo
        msg = msg +'|'+ str(self.nProgramOrd)
        msg = msg +'|'+ str(self.nX)
        msg = msg +'|'+ str(self.nY)
        msg = msg +'|'+ str(self.nAreaWidth)
        msg = msg +'|'+ str(self.nAreaHeight)

        # AddScreenProgramAreaBmpTextText
        # nScreenNo
        # nProgramOrd
        msg = msg +'|'+ str(self.nAreaOrd)

        msg = msg +'|'+ self.base64(self.pText)
        msg = msg +'|'+ str(self.nShowSingle)
        msg = msg +'|'+ str(self.nHorAlign)
        msg = msg +'|'+ str(self.nVerAlign)
        msg = msg +'|'+ self.base64(self.pFontName)
        msg = msg +'|'+ str(self.nFontSize)
        msg = msg +'|'+ str(self.nBold)
        msg = msg +'|'+ str(self.nItalic)
        msg = msg +'|'+ str(self.nUnderline)
        msg = msg +'|'+ str(self.nFontColor)

        msg = msg +'|'+ str(self.nStunt)
        msg = msg +'|'+ str(self.nRunSpeed)
        msg = msg +'|'+ str(self.nShowTime)
        msg = msg +'|'+ str(self.nStretch)
        msg = msg +'|'+ str(self.nShift)

        # SendScreenInfo
        # nScreenNo
        msg = msg +'|'+ str(self.nSendCmd)
        msg = msg +'|'+ str(self.nOtherParam1)

        #定时关机
        msg = msg +'|'+ str(self.nOnHour1)
        msg = msg +'|'+ str(self.nOnMinute1)
        msg = msg +'|'+ str(self.nOffHour1)
        msg = msg +'|'+ str(self.nOffMinute1)
        msg = msg +'|'+ str(self.nOnHour2)
        msg = msg +'|'+ str(self.nOnMinute2)
        msg = msg +'|'+ str(self.nOffHour2)
        msg = msg +'|'+ str(self.nOffMinute2)
        msg = msg +'|'+ str(self.nOnHour3)
        msg = msg +'|'+ str(self.nOnMinute3)
        msg = msg +'|'+ str(self.nOffHour3)
        msg = msg +'|'+ str(self.nOffMinute3)

        #调亮度
        msg = msg + '|' + str(self.nAdjustType)
        msg = msg + '|' + str(self.nHandleLight)
        msg = msg + '|' + str(self.nHour1)
        msg = msg + '|' + str(self.nMinute1)
        msg = msg + '|' + str(self.nLight1)
        msg = msg + '|' + str(self.nHour2)
        msg = msg + '|' + str(self.nMinute2)
        msg = msg + '|' + str(self.nLight2)
        msg = msg + '|' + str(self.nHour3)
        msg = msg + '|' + str(self.nMinute3)
        msg = msg + '|' + str(self.nLight3)
        msg = msg + '|' + str(self.nHour4)
        msg = msg + '|' + str(self.nMinute4)
        msg = msg + '|' + str(self.nLight4)

        return msg

    def run(self):

        # 发送===================================================================
        self.working = True
        requireclose = False

        self.result=""
        try:
            requireclose = False
            # 发送头信息
            client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client.settimeout(3)
            res=client.connect_ex((self.ledServerIP, self.ledServerPort))
            if res!=0 :
                return ''

            requireclose = True

            msg = self.toStr()
            forsend = msg.encode("UTF-8")  # 编码？？？
            client.sendall(forsend)
            msg = client.recv(1024)
            res = len(msg)
            self.result = msg.decode("UTF-8")

            #print(msg)

            self.working = False
            requireclose = False
            client.close() #发送完毕，断开链接

            return self.result
        except (Exception,IOError) as e:
            self.working = False
            Funcs.print("Error: 网络操作异常 ")
            logging.error(e)
            if requireclose:
                requireclose = False
                try:
                    client.close()
                except (Exception, IOError):
                    pass
            return self.result
        finally:
            if requireclose:
                client.close()


if __name__ == '__main__':
    obj = Task()

    obj.run()

    print(obj.result)
