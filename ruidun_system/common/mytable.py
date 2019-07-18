#coding=utf-8
import sys
import socket
import random
import time
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

class Feild:
    def __init__(self):
        #字段基本属性
        self._nm=''
        self._type=''
        self._size=0
        self._digits=0
        self._notnull=False

        #业务操作动态信息
        self._lbl=''
        self._input=''
        self._defa=''
        self._value=''
        self._express=''  #表达式，产生sql时优先

        self._isNull=False #null

    def setfld(self,lbl,nm,type,size,digits,notnull):
        self._lbl=lbl.strip()
        self._nm=nm.strip()
        self._type=type.strip()

        self._size=size
        self._digits=digits
        self._notnull=notnull

        self._input=self._nm #默认

        type = type.lower().strip() #仅处理常规字段
        if type.find('bit')>-1 :type='b' #01

        if type.find('int')>-1 :type='n'
        if type.find('real')>-1 :type='n'
        if type.find('double')>-1 :type='n'
        if type.find('float')>-1 :type='n'
        if type.find('decimal')>-1 :type='n'
        if type.find('numeric')>-1 :type='n'

        if type.find('char')>-1 :type='c'
        if type.find('text')>-1 :type='c'

        if type.find('date')>-1 :type='d'
        if type.find('time')>-1 :type='d'

        self._type=type

class Table:
    def __init__(self,tbl):
        self._table=tbl #表名
        self._flds=[] #表字段

        self._whereInput="__Where" #条件web字段，默认是__Where
        self._whereValue="" #条件值
        self._workflds=[] #当前业务字段

    #取字段
    def getfld(self,nm):
        nm = nm.lower().strip()
        if not self._flds: return None

        for fld in self._flds:
            if fld._nm.lower().strip()==nm:return fld
        return None

    #设置字段属性
    def setfld(self,lbl,nm,type,size=0,digits=0,notnull=False):
        fld=self.getfld(nm)
        if fld is None:
            fld=Feild()
            self._flds.append(fld)
        fld.setfld(lbl,nm,type,size,digits,notnull)

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

    #取数据
    def request(self,req,idx):
        suffix=""
        if idx>0 :suffix="__"+str(idx)

        self._whereValue = req.form.get(self._whereInput + suffix)

        for nm in self._workflds:
            fld=self.getfld(nm)
            if fld is None: continue
            fld._value = req.form.get(fld._input + suffix)

    #产生sql，跑出异常
    def sql(self):
        update="update "+self._table+" set "
        insert1="insert into "+self._table+" ("
        insert2=")values( "
        vstr=""
        sp=" "
        for nm in self._workflds:
            fld=self.getfld(nm)
            if fld is None: raise InputException(nm,'字段('+nm+ ")不存在")

            #取值
            v=fld._express #表达式优先
            if v=="" : v=fld._value
            if v=="" : v=fld._defa
            v=v.strip()

            #防sql注入
            v=v.replace("'","''")

            #格式化值
            #bit类型处理为01
            if fld._type=='b':
                if v=="":v='0'
                if v!="0" and fld._express!="" :v='1'

            #notnull检查
            if v=="" and fld._notnull :
                raise InputException(fld._input,fld._lbl + "不能为空")

            if fld._type=='d':
                try:
                    if ":" in v:
                        time.strptime(v, "%Y-%m-%d %H:%M:%S")
                        v = "STR_TO_DATE('" + v + "','%Y-%m-%d %H:%i:%s')"  # 输出：1992-04-12（日期形式）
                    else:
                        time.strptime(v, "%Y-%m-%d")
                        v = "STR_TO_DATE('" + v + "','%Y-%m-%d')"  # 输出：1992-04-12（日期形式）
                except:
                    raise InputException(fld._input, fld._lbl + "("+v+")格式不对")

            if fld._type=='c':
                vs = v.encode("gb2312")  # 编码？？？
                size=len(vs)
                if size>fld._size and fld._size > 0 :
                    raise InputException(fld._input,fld._lbl + "太长")
                v="'"+v+"'"

            if fld._type=='n':
                if v=="" :v="0"
                if not v.isdigit():raise InputException(fld._input,fld._lbl + "不是数字")

            #拼接sql
            update = update + sp + fld._nm + "=" + v
            insert1 = insert1 + sp + fld._nm
            insert2 = insert2 + sp + v
            sp=","

        self._whereValue = self._whereValue.strip()
        update = update + " where "+ self._whereValue
        insert = insert1 + insert2 + ")"

        if self._whereValue=="":
            return insert
        else:
            return update

