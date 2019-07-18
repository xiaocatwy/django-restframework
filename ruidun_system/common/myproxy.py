#coding=utf-8
import sys
import socket
import random
import time
import io
import json
import requests
import urllib
import threading
import logging
import pymysql as  MySQLdb
from DBUtils.PooledDB import PooledDB

from common.myfuncs import Funcs
from common.cfg import Config

class Proxy:

    @staticmethod
    def send(url,data):
        try:
            #s = json.dumps(data)
            r = requests.post(url, data=data)
            print(r.content)
            print(r.text)
            return r.text
        except:
            return  ""

    @staticmethod
    def sendExt(loginurl,logindata,url,data):
        try:
            #登录
            session = requests.session()
            r = session.post(loginurl, data=logindata)
            #print(r.text)

            #请求
            r = session.post(url, data=data)
            #r = session.get(url)
            #print(r.text)

            return r.text
        except:
            return  ""

    def __init__(self,url):
        self._url=url
        pass

    def get(self,url):
        try:
            r = requests.get(url)
            return r.text
        except:
            return  ""

    def post(self,data):
        try:
            r = requests.post(self._url, data=data)
            return r.text
        except:
            return  ""

    '''
    def postEx9(self,data):
        session = requests.session()
        r = session.post(self._url, data=data)
        #print(r.text)

        url = "http://192.168.0.158/position_sdk/ModularNowInfo/NowInfo/getAreaByCard"
        r = session.get(url)
        #print(r.text)

        return r.text

    def postEx8(self,data):
        session = requests.session()
        r = session.post(self._url, data=data)
        #print(r.text)

        url = "http://192.168.0.158/position_sdk/ModularNowInfo/NowInfo/getCardByArea"
        r = session.get(url)
        #print(r.text)

        return r.text

    def postEx3(self,data):
        session = requests.session()
        r = session.post(self._url, data=data)
        #print(r.text)

        url = "http://192.168.0.158/position_sdk/ModularNowInfo/NowInfo/getNowInfo"
        r = session.get(url)
        #print(r.text)

        return r.text

    def postEx2(self,data):
        session = requests.session()
        r = session.post(self._url, data=data)
        #print(r.text)

        url = "http://192.168.0.158/position_sdk/ModularNowInfo/NowInfo/getAllCardNowPos"
        r = session.get(url)
        #print(r.text)

        return r.text

    def postEx1(self,data):
        session = requests.session()
        r = session.post(self._url, data=data)
        #print(r.text)

        url = "http://192.168.0.158/position_sdk/ModularNowInfo/NowInfo/getAllAreaCardNum"
        r = session.get(url)
        #print(r.text)

        return r.text


    def getAllAreaCardID(self,data):
        session = requests.session()
        r = session.post(self._url, data=data)
        #print(r.text)

        url = "http://192.168.0.158/position_sdk/ModularNowInfo/NowInfo/getAllAreaCardID"
        r = session.get(url)
        #print(r.text)

        return r.text
     '''


