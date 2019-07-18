#coding=utf-8
from flask import Flask,request
import time
import pickle
import os,sys
import threading

from common.myfuncs import Funcs
from common.cfg import Config
import device.voicemp3
import device.switch
import device.led
from common.myproxy import Proxy

class Drv:
    def voice(self,data):
        task=device.voicemp3.Task()
        task.ip = data["ip"]
        task.port = data["port"]

        task.snlist = data["snlist"]
        task.voiceFilePath = data["voiceFilePath"]

        task.snlist=task.snlist.split(',')
        task.port=Funcs.toInt(task.port)
        task.start()
        return task

    def switch(self,data):
        task=device.switch.Task()
        task.ip = data["ip"]
        task.port = data["port"]

        task.cmd = data["cmd"]

        task.port=Funcs.toInt(task.port)
        result=task.run()
        return result

    def location(self,data):
        loginUrl=data["loginUrl"]
        logindata={}
        logindata["username"]=data["username"]
        logindata["password"]=data["password"]
        logindata["http_api_version"]=data["http_api_version"]

        url=data["cmd"]
        urldata = data
        del urldata['loginUrl']
        del urldata['username']
        del urldata['password']
        del urldata['http_api_version']
        del urldata['cmd']

        result=Proxy.sendExt(loginUrl,logindata,url,urldata)
        return result

    def led(self,data):
        _ini = Config()
        ip=_ini.get('main','ledServerIP')
        port=_ini.getint('main','ledServerPort')

        task=device.led.Task(ip,port)

        # AddScreen
        task.nControlType = data['nControlType']
        task.nScreenNo = data['nScreenNo']
        task.nSendMode = data['nSendMode']
        task.nWidth = data['nWidth']
        task.nHeight = data['nHeight']

        task.nScreenType = data['nScreenType']
        task.nPixelMode = data['nPixelMode']
        task.nDataDA = data['nDataDA']
        task.nDataOE = data['nDataOE']
        task.nRowOrder = data['nRowOrder']
        task.nDataFlow = data['nDataFlow']
        task.nFreqPar = data['nFreqPar']

        task.pCom = data['pCom']
        task.nBaud = data['nBaud']
        task.pSocketIP = data['pSocketIP']
        task.nSocketPort = data['nSocketPort']
        task.nStaticIPMode = data['nStaticIPMode']
        task.nServerMode = data['nServerMode']
        task.pBarcode = data['pBarcode']

        task.pNetworkID = data['pNetworkID']
        task.pServerIP = data['pServerIP']
        task.nServerPort = data['nServerPort']
        task.pServerAccessUser = data['pServerAccessUser']
        task.pServerAccessPassword = data['pServerAccessPassword']
        task.pWiFiIP = data['pWiFiIP']

        task.nWiFiPort = data['nWiFiPort']
        task.pGprsIP = data['pGprsIP']
        task.nGprsPort = data['nGprsPort']
        task.pGprsID = data['pGprsID']
        task.pScreenStatusFile = data['pScreenStatusFile']

        #AddScreenProgram
        # nScreenNo
        task.nProgramType = data['nProgramType']
        task.nPlayLength = data['nPlayLength']

        task.nStartYear = data['nStartYear']
        task.nStartMonth = data['nStartMonth']
        task.nStartDay = data['nStartDay']
        task.nEndYear = data['nEndYear']
        task.nEndMonth = data['nEndMonth']
        task.nEndDay = data['nEndDay']

        task.nMonPlay = data['nMonPlay']
        task.nTuesPlay = data['nTuesPlay']
        task.nWedPlay = data['nWedPlay']
        task.nThursPlay = data['nThursPlay']
        task.nFriPlay = data['nFriPlay']
        task.nSatPlay = data['nSatPlay']
        task.nSunPlay = data['nSunPlay']

        task.nStartHour = data['nStartHour']
        task.nStartMinute = data['nStartMinute']
        task.nEndHour = data['nEndHour']
        task.nEndMinute = data['nEndMinute']

        # AddScreenProgramBmpTextArea
        # task.nScreenNo
        task.nProgramOrd = data['nProgramOrd']
        task.nX = data['nX']
        task.nY = data['nY']
        task.nAreaWidth = data['nAreaWidth']
        task.nAreaHeight = data['nAreaHeight']


        # AddScreenProgramAreaBmpTextText
        # nScreenNo
        # nProgramOrd
        task.nAreaOrd = data['nAreaOrd']

        task.pText = data['pText']
        task.nShowSingle = data['nShowSingle']
        task.nHorAlign = data['nHorAlign']
        task.nVerAlign = data['nVerAlign']
        task.pFontName = data['pFontName']
        task.nFontSize = data['nFontSize']
        task.nBold = data['nBold']
        task.nItalic = data['nItalic']
        task.nUnderline = data['nUnderline']
        task.nFontColor = data['nFontColor']

        task.nStunt = data['nStunt']
        task.nRunSpeed = data['nRunSpeed']
        task.nShowTime = data['nShowTime']
        task.nStretch = data['nStretch']
        task.nShift = data['nShift']

        # SendScreenInfo
        # nScreenNo
        task.nSendCmd = data['nSendCmd']
        task.nOtherParam1 = data['nOtherParam1']

        #定时关机
        task.nOnHour1 = data['nOnHour1']
        task.nOnMinute1 = data['nOnMinute1']
        task.nOffHour1 = data['nOffHour1']
        task.nOffMinute1 = data['nOffMinute1']
        task.nOnHour2 = data['nOnHour2']
        task.nOnMinute2 = data['nOnMinute2']
        task.nOffHour2 = data['nOffHour2']
        task.nOffMinute2 = data['nOffMinute2']
        task.nOnHour3 = data['nOnHour3']
        task.nOnMinute3 = data['nOnMinute3']
        task.nOffHour3 = data['nOffHour3']
        task.nOffMinute3 = data['nOffMinute3']

        #调亮度
        task.nAdjustType = data['nAdjustType']
        task.nHandleLight = data['nHandleLight']
        task.nHour1 = data['nHour1']
        task.nMinute1 = data['nMinute1']
        task.nLight1 = data['nLight1']
        task.nHour2 = data['nHour2']
        task.nMinute2 = data['nMinute2']
        task.nLight2 = data['nLight2']
        task.nHour3 = data['nHour3']
        task.nMinute3 = data['nMinute3']
        task.nLight3 = data['nLight3']
        task.nHour4 = data['nHour4']
        task.nMinute4 = data['nMinute4']
        task.nLight4 = data['nLight4']


        result=task.run()
        return result