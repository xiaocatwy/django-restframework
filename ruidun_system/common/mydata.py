#coding=utf-8
import sys
import socket
import random
import time,datetime
import io
import threading
import logging
from flask import request

from common.myfuncs import Funcs

class InputException(Exception):
    '''自定义异常类'''
    input=""
    msg=""
    def __init__(self,input, msg):
        self.input = input
        self.msg = msg

class Table:
    def __init__(self,tbl,fld):
        self._table=tbl #表名
        self._flds = fld.split(',') #表字段     self._flds=[]
        self._workflds=self._flds
        self._whereInput="__Where" #条件web字段，默认是__Where
        self._whereValue="" #条件值

    #取字段
    def getfld(self,nm):
        nm = nm.lower().strip()
        if not self._flds: return None

        for fld in self._flds:
            if fld.lower().strip()==nm : return fld
        return None

    #设置where表达式
    def setwherevalue(self,express):
        self._whereValue = express.strip()

    #设置where对应的input
    def setwhereinput(self,input):
        self._whereInput = input.strip()

    #设置字段对应的label
    def setfldlbl(self,nm,lbl):
        fld=self.getfld(nm)
        if fld is None:return
        fld._lbl = lbl

    #设置字段对应的input
    def setfldinput(self,nm,input):
        fld=self.getfld(nm)
        if fld is None:return
        fld._input = input.strip()

    #设置字段对应的值
    def setfldvalue(self, nm, value):
        fld = self.getfld(nm)
        if fld is None: return
        fld._value = value.strip()

    #设置字段对应的默认值
    def setflddefa(self,nm,defa):
        fld=self.getfld(nm)
        if fld is None:return
        fld._defa = defa.strip()

    #设置字段对应的表达式值
    def setfldexpress(self,nm,express):
        fld=self.getfld(nm)
        if fld is None:return
        fld._express = express

    #设置当前操作字段
    def setfldstr(self,fldstr):
        self._workflds = fldstr.split(',')


    #产生sql，跑出异常
    def sql(self,row):

        t = time.time()
        d =  time.localtime(time.time())

        update="update "+self._table+" set "
        insert1="insert into "+self._table+" ("
        insert2=")values( "
        vstr=""
        sp=" "
        for nm in self._workflds:
            fld=self.getfld(nm)
            if fld is None: raise InputException(nm,'字段('+nm+ ")不存在")

            #取值
            v=row[nm]
            fldtype=type(v).__name__

            if fldtype=='bool':
                if v==True:
                    v='1'
                else:
                    v='0'

            elif fldtype=='datetime' or fldtype=='date' or fldtype=='time':
                try:
                    v=v.strftime("%Y-%m-%d %H:%M:%S")
                except:
                    v = time.strftime("%Y-%m-%d %H:%M:%S", v)

                v = "STR_TO_DATE('" + v + "','%Y-%m-%d %H:%i:%s')"  # 输出：1992-04-12（日期形式）
            elif fldtype=='str':
                v = v.strip()
                v=v.replace("'","''") ##防注入
                v="'"+v+"'"

            elif fldtype == 'int' or fldtype == 'float':
                v="'"+str(v)+"'"
            else:
                if v==None : v="null"

            #拼接sql
            update = update + sp + fld + "=" + v
            insert1 = insert1 + sp + fld
            insert2 = insert2 + sp + v
            sp=","


        if Funcs.isNoneOrEmpty(self._whereValue):
            insert = insert1 + insert2 + ")"
            return insert
        else:
            self._whereValue = self._whereValue.strip()
            update = update + " where "+ self._whereValue
            return update

