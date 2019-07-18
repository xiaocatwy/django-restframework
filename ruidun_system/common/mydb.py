#coding=utf-8
import sys
import socket
import random
import time
import io
import threading
import logging
import pymysql as  MySQLdb
from DBUtils.PooledDB import PooledDB

from common.myfuncs import Funcs
from common.cfg import Config

#
#高铭 201902013
#

class DB:
    #链接参数，系统初始化时赋值

    _ini=Config()

    '''
    _drive
    不同的SQL server版本对应的DRIVER字段不同。对应关系如下
    {SQL Server} - released with SQL Server 2000
    {SQL Native Client} - released with SQL Server 2005 (also known as version 9.0)
    {SQL Server Native Client 10.0} - released with SQL Server 2008
    {SQL Server Native Client 11.0} - released with SQL Server 2012
    '''

    _dbtype=_ini.get('conn','dbtype','mysql/mssql')
    _drive=_ini.get('conn','DRIVER','{SQL Server Native Client 11.0}')
    _mincached=_ini.getint('conn','mincached',5)
    _host=_ini.get('conn','host','localhost')
    _port=_ini.getint('conn','port',3306)
    _db=_ini.get('conn','database','ruidun')
    _user=_ini.get('conn','user','root')
    _passwd=_ini.get('conn','passwd','passwd')

    '''
    _mincached=5
    _host='localhost'
    _user='root'
    _passwd='gaoming'
    _db='ruidun'
    _port=3306
    '''

    #链接池
    _pool=None

    def __init__(self):
        #当前实例属性
        self._sqls=[]
        self._con=None
        self._cur=None

    def __del__(self):
        self._sqls=[]

        try:
            if not (self._cur is None):
                self._cur.close()
                self._cur=None
        except:
            pass

        try:
            if not (self._con is None):
                self._con.close()
                self._con=None
        except:
            pass


    def close(self):
        self._sqls=[]

        try:
            if not (self._cur is None):
                self._cur.close()
                self._cur=None
        except:
            pass

        try:
            if not (self._con is None):
                self._con.close()
                self._con=None
        except:
            pass

    def query(self, sql):
        try:
            if self._dbtype=='mssql':
                import pyodbc
                self._con = pyodbc.connect(r'DRIVER='+self._drive+';SERVER='+self._host+';DATABASE='+self._db+';UID='+self._user+';PWD='+self._passwd)
            else:
                if self._pool is None:self._pool = PooledDB(MySQLdb, self._mincached, host=self._host, user=self._user, passwd=self._passwd, db=self._db,port=self._port)  # 5为连接池里的最少连接数
                if self._pool is None:return None
                if self._con is None: self._con = self._pool.connection()
        except Exception as e:
            print(e)
        finally:
            if not self._con:return None
            if self._con is None: return None

        if self._con is None: return None
        conworking=True
        curworking=False

        rownumber=0
        flds=None
        data=None
        try:
            self._cur = self._con.cursor()
            curworking=True

            rownumber = self._cur.execute(sql)

            flds = self._cur.description
            data = self._cur.fetchall()

            self._cur.close()
            self._cur=None
            curworking=False

            self._con.close()
            self._con=None
            conworking=False
        except (Exception,IOError,SyntaxError,ValueError,AttributeError) as e:
            print(sql)
            print(e)
            pass
        except:
            pass
        finally:
            try:
                if curworking:
                    self._cur.close()
                    self._con=None
            except:
                pass

            try:
                if conworking:
                    self._con.close()
                    self._con=None
            except:
                pass

        if flds is None:return None

        colcount=len(flds)
        result = []
        for res in data:
            row = {}
            i = 0
            for i in range(colcount):
                row[flds[i][0]]= res[i]
                i=i+1
            result.append(row)

        return result


    def update(self,sqls):
        try:
            if self._dbtype=='mssql':
                import pyodbc
                self._con = pyodbc.connect(r'DRIVER='+self._drive+';SERVER='+self._host+';DATABASE='+self._db+';UID='+self._user+';PWD='+self._passwd)
            else:
                if self._pool is None:self._pool = PooledDB(MySQLdb, self._mincached, host=self._host, user=self._user, passwd=self._passwd, db=self._db,port=self._port)  # 5为连接池里的最少连接数
                if self._pool is None:return -1
                if self._con is None: self._con = self._pool.connection()
        except Exception as e:
            print(e)
        finally:
            if not self._pool:return -1
            if self._pool is None: return -1
            if not self._con:return -2
            if self._con is None: return -2


        conworking=True
        curworking=False
        reqcommit=False
        rownumber=0
        flds=None
        data=None
        sql=""
        try:
            self._cur = self._con.cursor()
            conworking=True

            if isinstance(sqls,str):sqls=[sqls]

            for sql in sqls:
                if sql is None:continue
                sql=sql.strip()
                if sql=="":continue

                rownumber += self._cur.execute(sql)
                reqcommit = True #提交数据

            if reqcommit :
                self._con.commit()
                reqcommit=False

            self._cur.close()
            self._cur=None
            curworking=False

            self._con.close()
            self._con=None
            conworking=False

            return rownumber
        except (Exception,IOError,SyntaxError,ValueError,AttributeError) as e:
            print(sql)
            print(e)
            return -3
        except:
            return -4
        finally:
            try:
                if reqcommit:
                    self._con.rollback()
                    reqcommit=False
            except:
                pass

            try:
                if curworking:
                    self._cur.close()
                    self._con = None
            except:
                pass

            try:
                if conworking:
                    self._con.close()
                    self._con = None
            except:
                pass


if __name__ == '__main__':
    obj = DB()

    #sql = 'select top 1 * from MYCARCOMERECORD '
    sql = 'select * from test '
    data=obj.query(sql)
    print(data)
    